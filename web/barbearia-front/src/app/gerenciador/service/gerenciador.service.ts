import { Funcionario, Servico } from './../models/gerenciador.model';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class GerenciadorService {
  // servicoUrl = 'http://localhost:8000/api/servico/';

  constructor(private http: HttpClient) {}

  listarServico() {
    return this.http.get<Servico[]>('/api/servico');
  }
}
