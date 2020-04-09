import { Component } from '@angular/core';
import { BackendService } from './backend.service';
import {Subscription} from 'rxjs';
import { FormBuilder, Validators, FormGroup  } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'front-end';
  isSubmitted = false;
  itemListSubs: Subscription;
  itemList;
  myForm: FormGroup;

  constructor(private backendApi: BackendService, private formBuilder: FormBuilder) {


    this.myForm = formBuilder.group({
      population: ['', Validators.required],
      timeToElapse: ['', Validators.required],
      reportedCases: ['', Validators.required],
      totalhospitalBeds: ['', Validators.required],
      periodType: ['', Validators.required]
    });

  }


  // tslint:disable-next-line:use-lifecycle-interface
  ngOnInit() {

    this.itemListSubs = this.backendApi
      .getSomething()
      .subscribe(res => {
          this.itemList = res;
          console.log(res);
        },
        console.error
      );
  }

  // tslint:disable-next-line:use-lifecycle-interface
  ngOnDestroy() {
    this.itemListSubs.unsubscribe();
  }

  get formControls() {
    return this.myForm.controls;
  }


  submit() {

    this.isSubmitted = true;
    if (this.myForm.invalid) {
      return;
    }

    console.log(this.myForm.value);
   // post to api

  }


}
