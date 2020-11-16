import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { GerenciadorComponent } from './gerenciador/gerenciador.component';
import { LoginComponent } from './login/login.component';
import { GerenciadorService } from './gerenciador/service/gerenciador.service';

@NgModule({
  declarations: [AppComponent, GerenciadorComponent, LoginComponent],
  imports: [BrowserModule, AppRoutingModule, HttpClientModule],
  providers: [GerenciadorService],
  bootstrap: [AppComponent],
})
export class AppModule {}
