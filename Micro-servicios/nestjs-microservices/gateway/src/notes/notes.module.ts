import { Module } from '@nestjs/common';
import { NotesController } from './notes.controller';
import { ClientsModule, Transport } from '@nestjs/microservices';
import { AuthModule } from '../auth/auth.module';

@Module({
  imports: [
    AuthModule,
    ClientsModule.register([
      {
        name: 'NOTES_SERVICE',
        transport: Transport.NATS,
        options: {
          servers: 'nats://localhost:4222',
        },
      },
    ]),
  ],
  controllers: [NotesController],
})
export class NotesModule {}
