<!--for the header of the admin panel-->
<div class="row header">

  <div class="col-lg-4">
    <h3 class="pt-2 ml-4 admin-panel-text">Admin Panel</h3>
  </div><!--class col-lg-4 end-->

  <div class="col-lg-8" id="settings">
       
  <?php 
    //for the top of the admin panel
    require_once 'top_nav.php'

  ;?>

  </div><!--class col-lg-8 end-->
</div><!--class header end-->

<div class="row m-0" id="establishment">

  <div class="col-lg-2 side-nav">
    
  <?php 
  //for the side nav of the admin panel
  require_once 'side_nav.php'

  ;?>

  </div><!--class col-lg-2 end-->
  <!--for the modal add in action-->
  <div class="Modal" v-if="modal">
     <button class="close mr-2 mt-2" @click="modal = false;">&times;</button>
     <div class="modalHeader p-2">
        <h4 class="ml-2">Add Establishment</h4>
     </div>
     <div class="modalBody p-3">
       <label>Hotel Name</label>
       <input type="text" class="form-control" v-model="establishmentInfo.name" placeholder="Hotel name...">
       <label>Location</label>
       <input type="text" class="form-control" v-model="establishmentInfo.location" placeholder="brgy, municipality">
        <label>Rates</label>
       <input type="text" class="form-control" v-model="establishmentInfo.rates" placeholder="eg.. 1,000 - 5,000">
        <label>Contact</label>
       <input type="number" class="form-control" v-model="establishmentInfo.contact">

      <input type="file" class="mt-2" id="file"  ref="filess" v-on:change="FileUpload()" class="form-control-file">
       <button class="add" @click="addEstablishment()">Add Establishment</button>

     </div><!--end clas modalBody-->
  </div><!--end class modal-->

  <!--for the modal delete in action-->
  <div class="Modal" v-if="modalDelete">
     <button class="close mr-2 mt-2" @click="modalDelete = false; clear();">&times;</button>

     <div class="modalHeader p-2">
        <h4 class="ml-2">Delete Establishment</h4>
     </div>

     <div class="modalBody p-3">
       <h6 class="text-center red">Are you sure you want to delete this data?</h6>
       
       <button class="cancel" @click="modalDelete = false">Cancel</button> 
       <button class="yes" @click="deleteEstablishment();modalDelete = false;">Yes</button>

     </div><!--end clas modalBody-->
  </div><!--end class modal-->

  <!--for the modal edit in action-->
  <div class="Modal" v-if="modalEdit">

     <button class="close mr-2 mt-2" @click="modalEdit = false; clear();">&times;
     </button>

     <div class="modalHeader p-2">
        <h4 class="ml-2">Edit Establishment</h4>
     </div>

     <div class="modalBody p-3">
       
       <label>Hotel Name</label>
       <input type="text" class="form-control" v-model="establishmentInfo.name" placeholder="Hotel name...">

       <label>Location</label>
       <input type="text" class="form-control" v-model="establishmentInfo.location" placeholder="brgy, street, municipality">
      <label>Rates</label>
       <input type="text" class="form-control" v-model="establishmentInfo.rates" placeholder="eg.. 1,000 - 5,000">

      <label>Contact</label>
      <input type="number" class="form-control" v-model="establishmentInfo.contact">
      <input type="file" class="mt-2" id="file"  ref="file" v-on:change="EditFileUpload()" class="form-control-file">
      <button class="edit mt-2" @click="editEstablishment();modalEdit = false;">Edit</button>

     </div><!--end clas modalBody-->
  </div><!--end class modal-->
  <div class="col-lg-10">
    <div class="page-name">
        <h4 class="p-2">Establishments |<span class="fa fa-building ml-2"></span>  |</h4>
    </div>
      <div class="card mt-4">
        <div class="card-header">

        <button  class="btn btn-success" @click="modal = true">Add <span class="fa fa-plus"></span>
        </button>

        <!--message for each ADDING,UPDATING AND DELETING data in table--> 
        <h6 class="pull-right alert alert-info p-2" v-if="message">{{message}}</h6>

      </div><!--card class end-->

        <div class="card-body">

        <!--input filed for filtering the data in table-->
         <input type="text"  class="form-control pull-right mb-2 filter" placeholder="Filter datas..." id="myInput" >

        <div class="table-responsive table-min-height">
          <table class=" table table-striped table-bordered ">
            <thead>
                    
                <th>Photo</th>
                <th>Hotel Name</th>
                <th>Location</th>
                <th>Rates</th>
                <th>Contact</th>
                <th class="text-center">Action</th>
                   
            </thead>
            <tbody id="myTable" >
              <tr v-for="hotel in hotels">
                <td class="max-spot-photo"><img class="spot-photo" v-bind:src="'<?php echo base_url();?>assets/images/' + hotel.photo"></td>
                <td>{{hotel.name}}</td>
                <td>{{hotel.location}}</td>
                <td>{{hotel.rates}}</td>
                <td>{{hotel.contact}}</td>
                <td class="min-td">
                        
                  <button class="btn-delete pull-right min-delete" @click="
                     establishmentInfo.id = hotel.id; modalDelete = true;"><span class="fa fa-trash"></span> Delete
                  </button>

                  <button class="btn-edit pull-right" @click="
                    establishmentInfo.id = hotel.id; 
                    establishmentInfo.name = hotel.name;
                    establishmentInfo.location = hotel.location;
                    establishmentInfo.rates = hotel.rates;
                    establishmentInfo.contact = hotel.contact;
                    modalEdit = true;"><span class="fa fa-edit"></span> Edit
                  </button>
                    
                </td>
                </tr>
              </tbody>
            </table>
            </div><!--class table-responsive end-->
         </div><!-- class card body end-->      
      </div><!-- class card end-->  
   </div><!--class col-lg-10 end-->
</div><!--class row end-->


