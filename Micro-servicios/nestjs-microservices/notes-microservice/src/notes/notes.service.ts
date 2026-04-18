/* eslint-disable @typescript-eslint/unbound-method */
/* eslint-disable @typescript-eslint/no-unsafe-return */
/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
/* eslint-disable @typescript-eslint/no-unsafe-call */
import { Injectable } from '@nestjs/common';
import { CreateNoteDto } from './dto/create-note.dto';
import { Model } from 'mongoose';
import { InjectModel } from '@nestjs/mongoose';
import { Note, NoteDocument } from './notes.Schema';

@Injectable()
export class NotesService {
  constructor(@InjectModel(Note.name) private noteModel: Model<NoteDocument>) {}
  async create(createNoteDto: CreateNoteDto): Promise<Note> {
    // eslint-disable-next-line @typescript-eslint/no-unsafe-return, @typescript-eslint/no-unsafe-member-access
    const newNote = await this.noteModel.create(createNoteDto);
    return newNote;
  }

  async findAll(userId: string) {
    return await this.noteModel.find({ userId }).exec();
  }
}
