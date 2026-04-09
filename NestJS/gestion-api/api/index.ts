import { NestFactory } from '@nestjs/core';
import { AppModule } from '../src/app.module.js';
import { ValidationPipe } from '@nestjs/common';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import serverless from 'serverless-http';

// LRU Cache pattern: cache the compiled app for performance across requests
let cachedHandler: any;

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // CORS Configuration - following security best practices
  app.enableCors({
    origin: process.env.ALLOWED_ORIGINS?.split(',') || '*',
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
    allowedHeaders: 'Content-Type, Accept, Authorization',
    credentials: true,
  });

  // Global validation pipe
  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,
      forbidNonWhitelisted: true,
    }),
  );

  // Swagger documentation
  const config = new DocumentBuilder()
    .setTitle('API de Gestión de Usuarios')
    .setDescription('API para gestionar usuarios con NestJS')
    .setVersion('1.0')
    .addTag('users', 'Endpoints relacionados con usuarios')
    .addTag('auth', 'Endpoints relacionados con autenticación')
    .build();

  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api', app, document);

  await app.init();
  
  const expressApp = app.getHttpAdapter().getInstance();
  return serverless(expressApp, {
    provider: 'aws', // Vercel uses AWS Lambda under the hood
  });
}

// Serverless handler with error handling
export default async (req: any, res: any) => {
  try {
    // Initialize handler if not cached (server-cache-lru pattern)
    if (!cachedHandler) {
      cachedHandler = await bootstrap();
    }
    return cachedHandler(req, res);
  } catch (error) {
    console.error('Serverless handler error:', error);
    res.statusCode = 500;
    res.end(JSON.stringify({ error: 'Internal Server Error' }));
  }
};
