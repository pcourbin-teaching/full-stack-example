import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProtagonistTableComponent } from './protagonist-table.component';

describe('ProtagonistTableComponent', () => {
  let component: ProtagonistTableComponent;
  let fixture: ComponentFixture<ProtagonistTableComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProtagonistTableComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProtagonistTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
