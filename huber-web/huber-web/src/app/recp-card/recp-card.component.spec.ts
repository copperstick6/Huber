import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RecpCardComponent } from './recp-card.component';

describe('RecpCardComponent', () => {
  let component: RecpCardComponent;
  let fixture: ComponentFixture<RecpCardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RecpCardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RecpCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
