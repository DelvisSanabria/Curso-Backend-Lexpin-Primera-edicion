/* eslint-disable @typescript-eslint/no-unsafe-assignment */
/* eslint-disable @typescript-eslint/no-unsafe-argument */
/* eslint-disable @typescript-eslint/no-unsafe-return */
import { Injectable } from '@nestjs/common';
/* import { CreateUserDto } from './dto/create-user.dto'; */
import { PrismaService } from '../prisma/prisma.service.js';

@Injectable()
export class UsersService {
  constructor(private prisma: PrismaService) {}

  findAll() {
    return this.prisma.user.findMany();
  }
  create(createUserDto: any) {
    // eslint-disable-next-line @typescript-eslint/no-unsafe-assignment
    const newUser = { ...createUserDto };
    return this.prisma.user.create({ data: newUser });
  }
}
