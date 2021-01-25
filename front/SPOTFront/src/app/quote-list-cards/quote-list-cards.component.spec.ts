import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { QuoteListCardsComponent } from './quote-list-cards.component';

describe('QuoteListCardsComponent', () => {
  let component: QuoteListCardsComponent;
  let fixture: ComponentFixture<QuoteListCardsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ QuoteListCardsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(QuoteListCardsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
