import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { QuoteGraphComponent } from './quote-graph.component';

describe('QuoteGraphComponent', () => {
  let component: QuoteGraphComponent;
  let fixture: ComponentFixture<QuoteGraphComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ QuoteGraphComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(QuoteGraphComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
