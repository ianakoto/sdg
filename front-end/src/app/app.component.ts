import { Component } from '@angular/core';
import { BackendService } from './backend.service';
import {Subscription} from 'rxjs';
import { FormBuilder, Validators, FormGroup  } from '@angular/forms';
import { HttpClient } from '@angular/common/http';


export interface Region {
  name: string;
  avgAge: number;
  avgDailyIncomeInUSD: number;
  avgDailyIncomePopulation: number;

}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'COVID-19 ESTIMATOR';
  isSubmitted = false;
  itemListSubs: Subscription;
  itemList;
  myForm: FormGroup;
  setRegion: Region;
  estimateresult;

  constructor(private backendApi: BackendService, private formBuilder: FormBuilder, private http: HttpClient) {


    this.myForm = formBuilder.group({
      population: ['', Validators.required],
      timeToElapse: ['', Validators.required],
      reportedCases: ['', Validators.required],
      totalHospitalBeds: ['', Validators.required],
      periodType: ['', Validators.required]
    });

  }


  // tslint:disable-next-line:use-lifecycle-interface
  ngOnInit() {

    this.itemListSubs = this.backendApi
      .getLogs()
      .subscribe(res => {
          this.itemList = res;

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



    // this.setRegion.name = 'Africa';
    // this.setRegion.avgAge = 19.7;
    // this.setRegion.avgDailyIncomeInUSD = 5;
    // this.setRegion.avgDailyIncomePopulation = 0.71;

    // tslint:disable-next-line:variable-name
    const region_data = {name: 'Africa', avgAge: 19.7, avgDailyIncomeInUSD: 5, avgDailyIncomePopulation: 0.71 };


    const formvalue =  this.myForm.value;


    const region = region_data;


    const putdata = {region, ...formvalue};


   // post to api
    this.backendApi
    .postEstimator(putdata)
    .subscribe(res => {
      this.estimateresult = JSON.stringify(res);

    });

  }


}
