import { Servico } from './models/gerenciador.model';
import { Component, OnInit } from '@angular/core';
import { GerenciadorService } from './service/gerenciador.service';

@Component({
  selector: 'app-gerenciador',
  templateUrl: './gerenciador.component.html',
  styleUrls: ['./gerenciador.component.scss'],
})
export class GerenciadorComponent implements OnInit {
  servicos: Array<Servico> = [];

  constructor(private gerenciadorService: GerenciadorService) {}

  ngOnInit(): void {
    this.getServico();
  }

  getServico() {
    this.gerenciadorService
      .listarServico()
      .subscribe((dados) => (this.servicos = dados));
  }
}
