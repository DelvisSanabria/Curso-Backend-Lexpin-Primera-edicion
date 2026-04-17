import { IsEmail, IsString, MinLength } from 'class-validator';

export class RegisterUserDto {
  @IsEmail({}, { message: 'El correo electronico no es valido' })
  email!: string;

  @IsString()
  @MinLength(2, { message: 'El nombre debe tener al menos dos caracteres' })
  name!: string;

  @IsString()
  @MinLength(6, { message: 'la contrasena debe tener al menos 6 caracteres' })
  password!: string;
}
