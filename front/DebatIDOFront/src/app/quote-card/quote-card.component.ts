import { Component, OnInit, Input, Inject, Optional  } from '@angular/core';

import { QuoteService, Quote } from '../../../DebatIDOAPI';

import { PORTAL_DATA } from '../overlay-with-injection.service';

@Component({
  selector: 'app-quote-card',
  templateUrl: './quote-card.component.html',
  styleUrls: ['./quote-card.component.scss']
})
export class QuoteCardComponent implements OnInit {

  @Input()
  public quoteID;
  @Input()
  public quote: Quote;
  @Input()
  public collapsed = false;

  
  public iconsType = {
    1: {
      "icon" : "exit_to_app",
      "color" : "red"
    },
    2: {
      "icon" : "done",
      "color" : "orange"
    },
    3 : {
      "icon" : "done_all",
      "color" : "green"
    },
    "default" : {
      "icon" : "done_all",
      "color" : "green"
    }
  };

  constructor(@Optional() @Inject(PORTAL_DATA) public overlay, private quoteService: QuoteService) { }

  ngOnInit(): void {
    if (this.quoteID != undefined){
      this.refresh();
    }

    if (this.overlay){
      this.quote = this.overlay.object;
    }
  }

  refresh(){
    this.quoteService.quotesQuoteIDGet(this.quoteID).subscribe(data => {
      this.quote = data;
    });
  }

}
