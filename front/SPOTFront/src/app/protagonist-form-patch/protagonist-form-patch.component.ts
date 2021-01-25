import { Component, OnInit, ViewChild, InjectionToken, Inject, Optional } from '@angular/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { MatInputModule } from '@angular/material/input';
import { FormsModule, FormBuilder, FormGroup } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatStepperModule, MatStepper } from '@angular/material/stepper';

import { ProtagonistService, Protagonist, Person, Company } from '../../../SPOTAPI';

import { PORTAL_DATA } from '../overlay-with-injection.service';

@Component({
  selector: 'app-protagonist-form-patch',
  templateUrl: './protagonist-form-patch.component.html',
  styleUrls: ['./protagonist-form-patch.component.scss']
})
export class ProtagonistFormPatchComponent implements OnInit {

  protagonistFormGroup: FormGroup;
  personFormGroup: FormGroup;
  companyFormGroup: FormGroup;
  @ViewChild('stepper') private stepper: MatStepper;

  protagonistTypes = Protagonist.TypeEnum;
  keys = Object.keys;

  constructor(@Inject(PORTAL_DATA) public overlay, private _formBuilder: FormBuilder, private protagonistService: ProtagonistService) { }

  ngOnInit() {
      this.formBuild();
  }

  formBuild(){
    this.protagonistFormGroup = this._formBuilder.group({
      type:[this.overlay.object.type],
      name:[this.overlay.object.name],
      link:[this.overlay.object.link],
      photo:[this.overlay.object.photo]
    });
    if (this.overlay.object.person){
      this.personFormGroup = this._formBuilder.group({
          surname:[this.overlay.object.person.surname],
          role:[this.overlay.object.person.role]
      });
    } else {
      this.personFormGroup = this._formBuilder.group({
          surname:[''],
          role:['']
      });
    }

    if (this.overlay.object.company){
      this.companyFormGroup = this._formBuilder.group({
          siret:[this.overlay.object.company.siret]
      });
    } else {
      this.companyFormGroup = this._formBuilder.group({
          siret:['']
      });
    }
  }

  onSubmitForm() {
    this.overlay.object.type = this.protagonistFormGroup.value.type;
    this.overlay.object.name = this.protagonistFormGroup.value.name;

    if (this.protagonistFormGroup.value.link) this.overlay.object.link = this.protagonistFormGroup.value.link;
    if (this.protagonistFormGroup.value.photo) this.overlay.object.photo = this.protagonistFormGroup.value.photo;

    if (this.overlay.object.type == 'person'){
      if (this.personFormGroup.value.surname) this.overlay.object.person.surname = this.personFormGroup.value.surname;
      if (this.personFormGroup.value.role) this.overlay.object.person.role = this.personFormGroup.value.role;
    }
    else if (this.overlay.object.type == 'company'){
      if (this.companyFormGroup.value.siret) this.overlay.object.company.siret = this.companyFormGroup.value.siret;
    }

    this.protagonistService.protagonistsProtagonistIDPatch(this.overlay.object.id,this.overlay.object).subscribe();
    this.overlay.overlay.detach();
  }

}
