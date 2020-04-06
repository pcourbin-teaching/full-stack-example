import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';

import { ReferenceService } from '../../../DebatIDOAPI/api/reference.service';
import { Reference } from '../../../DebatIDOAPI/model/reference';

@Component({
  selector: 'app-reference-table',
  templateUrl: './reference-table.component.html',
  styleUrls: ['./reference-table.component.scss']
})
export class ReferenceTableComponent implements OnInit {

  public columnsToDisplay = [ 'id', 'title', 'details', 'url', 'date', 'typeTitle', 'reliability' ];
  public references: MatTableDataSource<Reference>;
  constructor(private referenceService: ReferenceService) {
    referenceService.referenceGet().subscribe(data => {
      this.references = new MatTableDataSource<Reference>(data);
      this.references.sort = this.sort;
      this.references.paginator = this.paginator;
    });
  }

  @ViewChild(MatSort, {static: true}) sort: MatSort;
  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;

  ngOnInit(): void {
  }

}
