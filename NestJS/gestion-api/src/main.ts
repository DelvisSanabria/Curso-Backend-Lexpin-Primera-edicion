import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module.js';
import { ValidationPipe } from '@nestjs/common/pipes/index.js';
/* import { AuthGuard } from './users/guards/auth/auth.guard.js'; */

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true, // Elimina propiedades no definidas en el DTO
      forbidNonWhitelisted: true, // Lanza un error si se envían propiedades no definidas
      /* transform: true, // Transforma los payloads a los tipos definidos en los DTOs */
    }),
  );

  /* app.useGlobalGuards(AuthGuard); // Aquí puedes agregar tus guards globales si los tienes */
  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
