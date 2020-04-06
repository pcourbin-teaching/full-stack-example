/* https://dotnetthoughts.net/how-to-generate-angular-code-from-openapi-specifications/
https://github.com/swagger-api/swagger-codegen/blob/master/samples/client/petstore/typescript-angular-v4/npm/README.md
*/
import { Component, OnInit } from '@angular/core';

import { ThemeService } from '../../../api/api/theme.service';
import { Theme } from '../../../api/model/theme';

@Component({
  selector: 'app-theme',
  templateUrl: './theme.component.html',
  styleUrls: ['./theme.component.scss']
})
export class ThemeComponent implements OnInit {

  public themes: Theme[];
  constructor(private themeService: ThemeService) {
    themeService.themeGet().subscribe(data => {
      this.themes = data;
      console.log("Themes: ", data);
    });
  }

  ngOnInit(): void {
  }

  title = 'hello-world';

}
