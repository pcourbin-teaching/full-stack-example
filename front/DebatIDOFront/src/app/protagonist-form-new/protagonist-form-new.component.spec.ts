import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProtagonistFormNewComponent } from './protagonist-form-new.component';

describe('ProtagonistFormNewComponent', () => {
  let component: ProtagonistFormNewComponent;
  let fixture: ComponentFixture<ProtagonistFormNewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProtagonistFormNewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProtagonistFormNewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
