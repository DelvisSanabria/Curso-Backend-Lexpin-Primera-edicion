/* eslint-disable @typescript-eslint/no-unsafe-return */
import { Controller, Get, Post, Body } from '@nestjs/common';
import { UsersService } from './users.service.js';
/* import { CreateUserDto } from './dto/create-user.dto'; */

@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Get()
  findAll() {
    // eslint-disable-next-line @typescript-eslint/no-unsafe-call
    return this.usersService.findAll();
  }

  //para definir una ruta post usamos el decorador @Post
  @Post()
  create(@Body() createUserDto: any) {
    // eslint-disable-next-line @typescript-eslint/no-unsafe-return, @typescript-eslint/no-unsafe-call
    return this.usersService.create(createUserDto);
  }
}
