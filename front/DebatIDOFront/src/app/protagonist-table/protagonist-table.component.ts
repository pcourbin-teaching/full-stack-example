import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';

import { ProtagonistService, Protagonist } from '../../../DebatIDOAPI';

@Component({
  selector: 'app-protagonist-table',
  templateUrl: './protagonist-table.component.html',
  styleUrls: ['./protagonist-table.component.scss']
})
export class ProtagonistTableComponent implements OnInit {

  public columnsToDisplay = [ 'id', 'name', 'link', 'type', 'photo' ];
  public protagonists: MatTableDataSource<Protagonist>;
  constructor(private protagonistService: ProtagonistService) {
    protagonistService.protagonistGet().subscribe(data => {
      this.protagonists = new MatTableDataSource<Protagonist>(data);
      this.protagonists.sort = this.sort;
      this.protagonists.paginator = this.paginator;
    });
  }

  @ViewChild(MatSort, {static: true}) sort: MatSort;
  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;

  ngOnInit(): void {
  }

}
