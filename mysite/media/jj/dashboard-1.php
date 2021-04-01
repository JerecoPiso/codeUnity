<!--for the header of the admin panel-->
<div class="row header">

  <div class="col-lg-4">
		<h3 class="pt-2 ml-4 admin-panel-text">Admin Panel</h3>
  </div><!--class col-lg-4 end-->

  <div class="col-lg-8" id="settings">
			      
  <?php 
    //for the side nav of the admin panel
    require_once 'top_nav.php'

  ;?>
  </div><!--class col-lg-8 end-->
</div><!--class header end-->

<div class="row m-0" id="home_dashboard">

  <div class="col-lg-2 side-nav">
  	
	<?php 
	//for the side nav of the admin panel
	require_once 'side_nav.php'

	;?>

  </div><!--class col-lg-2 end-->
  <div class="Modal" v-if="modal">
       <button class="close mr-2 mt-2" @click="modal = false">&times;</button>
       <div class="modalHeader p-2">
          <h4 class="ml-2">List of Tourist Spots</h4>
       </div>
       <div class="modalBody p-3 max-list-height">
         
         <ul class="list-group">
           <li class="list-group-item" v-for="spot in spots">{{spot.name + " ( " + spot.municipality + " )"}}</li>
          
         </ul>

       </div><!--end class modalBody-->
    </div><!--end class modal-->
    <div class="Modal" v-if="modalEstablishment">
       <button class="close mr-2 mt-2" @click="modalEstablishment = false">&times;</button>
       <div class="modalHeader p-2">
          <h4 class="ml-2">List of Establishments</h4>
       </div>
       <div class="modalBody p-3 max-list-height">
         
         <ul class="list-group">
           <li class="list-group-item" v-for="hotel in hotels">{{hotel.name + " ( " + hotel.location + " )"}}</li>
      
         </ul>

       </div><!--end class modalBody-->
    </div><!--end class modal-->
     <div class="Modal" v-if="modalMunicipality">
       <button class="close mr-2 mt-2" @click="modalMunicipality = false">&times;</button>
       <div class="modalHeader p-2">
          <h4 class="ml-2">List of Municipalities</h4>
       </div>
       <div class="modalBody p-3 max-list-height">
         
         <ul class="list-group">
           <li class="list-group-item" v-for="mun in municipalities">{{mun.name}}</li>
      
         </ul>

       </div><!--end class modalBody-->
    </div><!--end class modal-->
  <div class="col-lg-10">
       <!--for the modal add in action-->
  
      <div class="row mt-3">
        <div class="col-lg-4 mt-2">
          <div class="card tourist-card" >
            <div class="card-header">
              <h4 class="card-title">Total Tourist Spot <span class="fa fa-plane pull-right"></span></h4>
            </div>
            <div class="card-body">
              <h5 class="total">{{totals.spot}} <button class="pull-right see-list" @click="modal = true">See list..</button></h5>
            </div>
          </div>
        </div>
        <div class="col-lg-4 mt-2">
          <div class="card establishment-card">
            <div class="card-header">
               <h4  class="card-title">Total Establishment <span class="fa fa-building pull-right"></span></h4>
            </div>
            <div class="card-body">
                <h5 class="total">{{totals.estab}} <button class="pull-right see-list"@click="modalEstablishment = true;">See list..</button></h5>
            </div>
          </div>
        </div>
        <div class="col-lg-4 mt-2">
          <div class="card municipalities-card" >
            <div class="card-header ">
               <h4  class="card-title"> Total Municipalities <span class="fa fa-map-marker pull-right"></span></h4>
            </div>
            <div class="card-body">
                <h5 class="total">{{totals.mun}} <button class="pull-right see-list" @click="modalMunicipality = true">See list..</button></h5>
            </div>
          </div>
        </div>

        <div class="col-lg-4 mt-4">
          <div class="card admins-card" >
            <div class="card-header ">
               <h4  class="card-title"> Total Admin Users<span class="fa fa-users pull-right"></span></h4>
            </div>
            <div class="card-body">
                <h5 class="total">{{totals.admin}} <button class="pull-right see-list"></button></h5>
            </div>
          </div>
        </div>

        <div class="col-lg-4 mt-4">

          <button v-b-tooltip.hover title="Print spots according to municipalities" @click="print()" class="btn-print"><span class="fa fa-print"></span> Print</button>

        </div>

        
      </div><!--class row end-->

	   
  </div><!--class col-lg-10 end-->

</div><!--class row end-->


