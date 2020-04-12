import { TestBed } from '@angular/core/testing';

import { OverlayWithInjectionService } from './overlay-with-injection.service';

describe('OverlayWithInjectionService', () => {
  let service: OverlayWithInjectionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(OverlayWithInjectionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
