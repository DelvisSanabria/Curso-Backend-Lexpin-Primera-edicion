import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module.js';
import { ValidationPipe } from '@nestjs/common';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';

// LRU Cache pattern: cache the compiled app for performance across requests
let cachedHandler: any;
let isBootstrapping = false;

async function bootstrap() {
  if (isBootstrapping) {
    // Esperar si ya se está inicializando
    while (isBootstrapping) {
      await new Promise(resolve => setTimeout(resolve, 100));
    }
    return cachedHandler;
  }

  isBootstrapping = true;

  try {
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
    
    // Import serverless-http dynamically
    const serverlessModule = await import('serverless-http');
    const serverless = serverlessModule.default || serverlessModule;
    
    const handler = serverless(expressApp, {
      provider: 'aws',
    });

    isBootstrapping = false;
    return handler;
  } catch (error) {
    isBootstrapping = false;
    console.error('Bootstrap error:', error);
    throw error;
  }
}

// Serverless handler with error handling
export default async (req: any, res: any) => {
  try {
    // Initialize handler if not cached (server-cache-lru pattern)
    if (!cachedHandler) {
      cachedHandler = await bootstrap();
    }
    return cachedHandler(req, res);
  } catch (error: any) {
    console.error('Serverless handler error:', error);
    res.statusCode = 500;
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({ 
      error: 'Internal Server Error',
      message: error?.message || 'Unknown error',
      timestamp: new Date().toISOString()
    }));
  }
};
