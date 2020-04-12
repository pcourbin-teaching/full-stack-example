import { Component, OnInit, ViewChild } from '@angular/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { MatInputModule } from '@angular/material/input';
import { FormsModule, FormBuilder, FormGroup } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatStepperModule, MatStepper } from '@angular/material/stepper';

import { ProtagonistService, Protagonist, Person, Company } from '../../../DebatIDOAPI';

@Component({
  selector: 'app-protagonist-form-new',
  templateUrl: './protagonist-form-new.component.html',
  styleUrls: ['./protagonist-form-new.component.scss']
})

export class ProtagonistFormNewComponent implements OnInit {

  protagonistFormGroup: FormGroup;
  personFormGroup: FormGroup;
  companyFormGroup: FormGroup;
  @ViewChild('stepper') private stepper: MatStepper;

  name = 'Angular';
  protagonistTypes = Protagonist.TypeEnum;
  keys = Object.keys;

  constructor(private _formBuilder: FormBuilder, private protagonistService: ProtagonistService) {}

  ngOnInit() {
      this.formBuild();
  }

  formBuild(){
    this.protagonistFormGroup = this._formBuilder.group({
      type:[''],
      name:[''],
      link:[''],
      photo:['']

    });
    this.personFormGroup = this._formBuilder.group({
      surname:[''],
      role:['']
    });
    this.companyFormGroup = this._formBuilder.group({
      siret:['']
    });
  }

  onSubmitForm() {
    let myNew = {} as Protagonist;
    console.log(Protagonist.TypeEnum);
    console.log(this.protagonistFormGroup.value);
    console.log(this.personFormGroup.value);
    console.log(this.companyFormGroup.value);

    myNew.type = this.protagonistFormGroup.value.type;
    myNew.name = this.protagonistFormGroup.value.name;
    if (this.protagonistFormGroup.value.link) myNew.link = this.protagonistFormGroup.value.link;
    if (this.protagonistFormGroup.value.photo) myNew.photo = this.protagonistFormGroup.value.photo;

    if (myNew.type == 'person'){
      let subMyNew = {} as Person;
      if (this.personFormGroup.value.surname) subMyNew.surname = this.personFormGroup.value.surname;
      if (this.personFormGroup.value.role) subMyNew.role = this.personFormGroup.value.role;
      myNew.person = subMyNew;
    }
    else if (myNew.type == 'company'){
      let subMyNew = {} as Company;
      if (this.companyFormGroup.value.siret) subMyNew.siret = this.companyFormGroup.value.siret;
      myNew.company = subMyNew;
    }

    this.protagonistService.protagonistPost(myNew).subscribe();
    this.stepper.reset();
  }

}
