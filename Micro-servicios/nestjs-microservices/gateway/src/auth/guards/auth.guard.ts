/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable @typescript-eslint/no-unsafe-call */
/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
import { Injectable, CanActivate, ExecutionContext, Inject, UnauthorizedException } from "@nestjs/common";
import { ClientProxy } from "@nestjs/microservices";
import { firstValueFrom } from "rxjs";
@Injectable()
export class AuthGuard implements CanActivate {
  constructor(
    @Inject('AUTH_SERVICE') private readonly authClient: ClientProxy,
  ) {}
  async canActivate(context: ExecutionContext): Promise<boolean> {
    const request = context.switchToHttp().getRequest();
    const authHeader = request.headers['authorization'];
    if (!authHeader) {
      throw new UnauthorizedException('No hay token de autenticación');
    }

    const token = authHeader.split(' ')[1];
    try {
      const userPayload = await firstValueFrom(
        this.authClient.send('auth.verify.user', token),
      );

      console.log('AuthGuard - userPayload from verify:', JSON.stringify(userPayload));
      request.user = userPayload;
      return true;
    } catch (error) {
      throw new UnauthorizedException(
        'No se pudo conectar al servicio de autenticación',
      );
    }
  }
}
