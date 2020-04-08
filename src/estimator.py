def estimator(data):
      
      """ THis function computes the estimation of covid 19 infected patients
      
      input: data as a dict
      
      data : 1. region as a dict
                            region: i. name as string
                                    ii. avgAge as double
                                    iii. avgDailyIncomeInUSD as double
                                    iv. avgDailyIncomePopulation as double

             2. periodType as string
             3. timeToElapse as an int
             4. reportedCases as an int
             5. population as an int
             6. totalHospitalBeds: as an int

       returns   a dictionary of input data, impact as dict, and severImpact as dict    
      
       """
      # normalize timeToElapse to days
      ptype = data.periodType;
      new_timeToElapse = 0;
      if ptype == "months":
            new_timeToElapse = 30 * data.timeToElapse;
      elif ptype == "weeks":
            new_timeToElapse = 7 * data.timeToElapse;
      else:
            new_timeToElapse = data.timeToElapse;
      
      factor = new_timeToElapse // 3;
            

      impact, severeImpact = dict({})

      impact['currentlyInfected'] = data.reportedCases * 10;
      severeImpact['currentlyInfected'] = data.reportedCases * 50;

      est_infectedPeople_impact = impact.currentlyInfected * (2 * factor); 
      est_infectedPeople_severeImpact = severeImpact.currentlyInfected * (2 * factor);
      
      impact['infectionsByRequestedTime'] = est_infectedPeople_impact;
      impact['severeCasesByRequestedTime '] = (impact.infectionsByRequestedTime * 15) / 100;
      
      severeImpact['infectionsByRequestedTime'] = est_infectedPeople_severeImpact;
      severeImpact['severeCasesByRequestedTime'] =(severeImpact.infectionsByRequestedTime * 15) / 100;

      totalHospitalBeds = (data.totalHospitalBeds * 95) / 100;
      occupied_beds = (totalHospitalBeds * 65) / 100;
      unoccupied_beds_covid_patients = totalHospitalBeds - occupied_beds;

      impact['hospitalBedsByRequestedTime'] = unoccupied_beds_covid_patients - impact.severeCasesByRequestedTime;
      severeImpact['hospitalBedsByRequestedTime'] = unoccupied_beds_covid_patients - severeImpact.severeCasesByRequestedTime;

      impact['casesForICUByRequestedTime'] = (impact.infectionsByRequestedTime * 5) / 100;
      severeImpact['casesForICUByRequestedTime '] = (severeImpact.infectionsByRequestedTime * 5) / 100;


      impact['casesForVentilatorsByRequestedTime'] = (impact.infectionsByRequestedTime * 2) / 100;
      severeImpact['casesForVentilatorsByRequestedTime'] = (severeImpact.infectionsByRequestedTime * 2) / 100;

      daily_income = data.region.avgDailyIncomeInUSD;
      avd_income_population = data.region. avgDailyIncomePopulation;


      impact['dollarsInFlight'] = impact.infectionsByRequestedTime * daily_income * avd_income_population * new_timeToElapse;  
      severeImpact['severeCasesByRequestedTime'] = severeImpact.infectionsByRequestedTime * daily_income * avd_income_population * new_timeToElapse;

      output = {'impact':impact,'severeImpact':severeImpact};


      return output
      
       
