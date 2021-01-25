import { Component, OnInit } from '@angular/core';

import { QuoteService, Quote } from '../../../SPOTAPI';

@Component({
  selector: 'app-quote-list-cards',
  templateUrl: './quote-list-cards.component.html',
  styleUrls: ['./quote-list-cards.component.scss']
})
export class QuoteListCardsComponent implements OnInit {
  
  public quotes;

  constructor(private quoteService: QuoteService) {
    quoteService.quoteGet().subscribe(data => {
      this.quotes = data;
    });
  }

  ngOnInit(): void {
  }

}
