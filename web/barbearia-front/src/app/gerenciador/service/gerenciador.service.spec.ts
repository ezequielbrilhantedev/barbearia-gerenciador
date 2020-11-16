import { TestBed } from '@angular/core/testing';

import { GerenciadorService } from './gerenciador.service';

describe('GerenciadorService', () => {
  let service: GerenciadorService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GerenciadorService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
