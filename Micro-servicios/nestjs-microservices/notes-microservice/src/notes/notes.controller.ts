/* eslint-disable @typescript-eslint/no-unsafe-return */
import { Controller } from '@nestjs/common';
import { NotesService } from './notes.service';
import { MessagePattern, Payload } from '@nestjs/microservices';
import { CreateNoteDto } from './dto/create-note.dto';

@Controller('notes')
export class NotesController {
  constructor(private readonly notesService: NotesService) {}
  @MessagePattern('notes.create')
  createNote(@Payload() CreateNoteDto: CreateNoteDto) {
    console.log('CreateNoteDto received:', JSON.stringify(CreateNoteDto));
    return this.notesService.create(CreateNoteDto);
  }

  @MessagePattern('notes.findAll')
  findAll(@Payload() userId: string) {
    return this.notesService.findAll(userId);
  }
}
