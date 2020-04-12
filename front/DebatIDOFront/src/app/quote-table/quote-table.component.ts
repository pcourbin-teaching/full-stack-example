import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';

import { QuoteService, Quote } from '../../../DebatIDOAPI';

@Component({
  selector: 'app-quote-table',
  templateUrl: './quote-table.component.html',
  styleUrls: ['./quote-table.component.scss']
})
export class QuoteTableComponent implements OnInit {

  public columnsToDisplay = [ 'id', 'typeTitle', 'title', 'details' ];
  public quotes: MatTableDataSource<Quote>;

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

  constructor(private quoteService: QuoteService) {
    quoteService.quoteGet().subscribe(data => {
      this.quotes = new MatTableDataSource<Quote>(data);
      this.quotes.sort = this.sort;
      this.quotes.paginator = this.paginator;
    });
  }

  @ViewChild(MatSort, {static: true}) sort: MatSort;
  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;

  ngOnInit(): void {
  }

}
