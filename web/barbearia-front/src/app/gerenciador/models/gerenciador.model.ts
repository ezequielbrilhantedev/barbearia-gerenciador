export interface Servico {
  funcionario: Funcionario[];
  corte: Corte[];
  barba: Barba[];
}

export interface Funcionario {
  nome: string;
}

export interface Corte {
  tipo_de_corte: string;
}

export interface Barba {
  barba: string;
}
