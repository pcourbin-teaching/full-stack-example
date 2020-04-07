/* https://dotnetthoughts.net/how-to-generate-angular-code-from-openapi-specifications/
https://github.com/swagger-api/swagger-codegen/blob/master/samples/client/petstore/typescript-angular-v4/npm/README.md
*/
import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';

import { ThemeService, Theme } from '../../../DebatIDOAPI';


@Component({
  selector: 'app-theme-table',
  templateUrl: './theme-table.component.html',
  styleUrls: ['./theme-table.component.scss']
})
export class ThemeTableComponent implements OnInit {

  public columnsToDisplay = ['id', 'title'];
  public themes: MatTableDataSource<Theme>;
  constructor(private themeService: ThemeService) {
    themeService.themeGet().subscribe(data => {
      this.themes = new MatTableDataSource<Theme>(data);
      this.themes.sort = this.sort;
      this.themes.paginator = this.paginator;
    });
  }

  @ViewChild(MatSort, {static: true}) sort: MatSort;
  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;

  ngOnInit(): void {
  }

}
