import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { environment } from '../environments/environment';

import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MatSliderModule } from '@angular/material/slider';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';
import { MatTabsModule } from '@angular/material/tabs';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatStepperModule } from '@angular/material/stepper';
import { FormBuilder, FormGroup } from '@angular/forms';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { OverlayModule } from '@angular/cdk/overlay';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatGridListModule } from '@angular/material/grid-list';

import { ThemeTableComponent } from './theme-table/theme-table.component';
import { ProtagonistTableComponent } from './protagonist-table/protagonist-table.component';
import { QuoteTableComponent } from './quote-table/quote-table.component';
import { ReferenceTableComponent } from './reference-table/reference-table.component';
import { QuoteGraphComponent } from './quote-graph/quote-graph.component';

import { ApiModule, Configuration, ConfigurationParameters } from '../../SPOTAPI';
import { BASE_PATH } from '../../SPOTAPI/variables';
import { ThemeFormNewComponent } from './theme-form-new/theme-form-new.component';
import { ProtagonistFormNewComponent } from './protagonist-form-new/protagonist-form-new.component';
import { ThemeFormPatchComponent } from './theme-form-patch/theme-form-patch.component';
import { ProtagonistFormPatchComponent } from './protagonist-form-patch/protagonist-form-patch.component';
import { ReferenceSmallComponent } from './reference-small/reference-small.component';
import { QuoteCardComponent } from './quote-card/quote-card.component';
import { QuoteListCardsComponent } from './quote-list-cards/quote-list-cards.component';

export function apiConfigFactory() {
    const params: ConfigurationParameters = {
      apiKeys: environment.API_KEYS, //{"API-KEY": "G#hqqq8NlW&tz5Hjk#%qcr7^iV*P%2pZWd*!mafPpu5!ANjJwM"},
  //    username?: string;
  //    password?: string;
  //    accessToken?: string | (() => string);
      basePath: environment.API_BASE_PATH,
  //    withCredentials?: boolean;
  //    encoder?: HttpParameterCodec;
    };
    return new Configuration(params);
}
/*
export function apiConfigFactory (): Configuration => {
  const params: ConfigurationParameters = {
    apiKeys: environment.API_KEYS,
    basePath: environment.API_BASE_PATH,
    // set configuration parameters here.
  }
  return new Configuration(params);
}
*/

@NgModule({
  declarations: [
    AppComponent,
    ThemeTableComponent,
    ProtagonistTableComponent,
    QuoteTableComponent,
    ReferenceTableComponent,
    QuoteGraphComponent,
    ThemeFormNewComponent,
    ProtagonistFormNewComponent,
    ThemeFormPatchComponent,
    ProtagonistFormPatchComponent,
    ReferenceSmallComponent,
    QuoteCardComponent,
    QuoteListCardsComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    ApiModule.forRoot(apiConfigFactory),
    BrowserAnimationsModule,
    MatSliderModule,
    MatTableModule,
    MatTabsModule,
    MatPaginatorModule,
    MatSortModule,
    MatExpansionModule,
    MatFormFieldModule,
    MatSelectModule,
    MatInputModule,
    MatButtonModule,
    MatStepperModule,
    FormsModule,
    ReactiveFormsModule,
    OverlayModule,
    MatIconModule,
    MatCardModule,
    MatGridListModule,
  ],
  providers: [ ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
