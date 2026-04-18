/* eslint-disable @typescript-eslint/no-unsafe-argument */
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
/* eslint-disable @typescript-eslint/no-unsafe-member-access */
import {
  Controller,
  Get,
  Post,
  Body,
  Inject,
  UseGuards,
  Request,
} from '@nestjs/common';
import { ClientProxy } from '@nestjs/microservices';
import { CreateNoteDto } from './dto/create-note.dto';
import { AuthGuard } from '../auth/guards/auth.guard';

@Controller('notes')
export class NotesController {
  constructor(
    @Inject('NOTES_SERVICE') private readonly notesClient: ClientProxy,
  ) {}

  @Post()
  @UseGuards(AuthGuard)
  createNote(@Body() createNoteDto: CreateNoteDto, @Request() req) {
    const userId = String(req.user.id);
    const payload = {
      ...createNoteDto,
      userId: userId,
    };
    console.log('Gateway - Sending to notes.create:', JSON.stringify(payload));
    return this.notesClient.send('notes.create', payload);
  }

  @Get()
  @UseGuards(AuthGuard)
  findAll(@Request() req: any) {
    const userId = String(req.user.id);
    return this.notesClient.send('notes.findAll', userId);
  }
}
