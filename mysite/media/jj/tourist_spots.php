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

<div class="row m-0" id="touristSpot">

  <div class="col-lg-2 side-nav">
    
  <?php 
  //for the side nav of the admin panel
  require_once 'side_nav.php'

  ;?>

  </div><!--class col-lg-2 end-->

  <!--for the modal add in action-->
  <div class="Modal" v-if="modal">
     <button class="close mr-2 mt-2" @click="modal = false; clear();">&times;
     </button>
     <div class="modalHeader p-2">
        <h4 class="ml-2">Add Spot</h4>
     </div>
     <div class="modalBody p-3">

       <label>Spot Name</label>
       <input type="text" class="form-control" v-model="spotInfo.name">

       <label>Municipality</label>
       <select class="custom-select" v-model="spotInfo.municipality">
         <option v-for="municipality in municipalities">{{municipality.name + ' ( ' + municipality.dist_name + ' )'}}</option>
       </select>
       <label>Category</label>
       <select class="custom-select"  v-model="spotInfo.category">
         <option v-for="category in categories">{{category.name}}</option>
       </select>

        <input type="file" class="mt-2" id="file"  ref="file" v-on:change="handleFileUpload()" class="form-control-file">

       <button class="add" @click="addSpot()">Add Spot</button>

     </div><!--end class modalBody-->
</div><!--end class modal-->

  <!--for the modal delete in action-->
  <div class="Modal" v-if="modalDelete">
     <button class="close mr-2 mt-2" @click="modalDelete = false; clear();">&times;</button>

     <div class="modalHeader p-2">
        <h4 class="ml-2">Delete Spot</h4>
     </div>

     <div class="modalBody p-3">

       <h6 class="text-center red">Are you sure you want to delete this data?</h6>
       
       <button class="cancel" @click="modalDelete = false">Cancel</button> 
       <button class="yes" @click="deleteSpot();modalDelete = false;">Yes</button>

   </div><!--end class modalBody-->
</div><!--end class modal-->

  <!--for the modal edit in action-->
  <div class="Modal" v-if="modalEdit">
     <button class="close mr-2 mt-2" @click="modalEdit = false; clear();">&times;</button>

     <div class="modalHeader p-2">
        <h4 class="ml-2">Edit Spot</h4>
     </div>

     <div class="modalBody p-3">
       
       <label>Spot Name</label>
       <input type="text" class="form-control" v-model="spotInfo.name">

       <label>Municipality</label>
       <select class="custom-select" v-model="spotInfo.municipality">
         <option v-for="municipality in municipalities">{{municipality.name + ' ( ' + municipality.dist_name + ' )'}}</option>
       </select>
       
       <label>Category</label>
       <select class="custom-select"  v-model="spotInfo.category">
         <option v-for="category in categories">{{category.name}}</option>
       </select>

       <input type="file" class="mt-2" id="file"  ref="files" v-on:change="handleEditFile()" class="form-control-file">

       <button class="edit mt-2" @click="editSpot();modalEdit = false;">Edit</button>

    </div><!--end class modalBody-->
</div><!--end class modal-->
  
  <div class="col-lg-10">
   <div class="page-name">
        <h4 class="p-2">Tourist Spots in Leyte |<span class="fa fa-plane ml-2"></span>  |</h4>
    </div>
     <div class="card mt-4">
      <div class="card-header">

        <button  class="btn btn-success" @click="modal = true">Add 
           <span class="fa fa-plus"></span>
        </button>
        <!--message for each ADDING,UPDATING AND DELETING data in table-->
        <h6 class="pull-right alert alert-info p-2" v-if="message" >{{message}}</h6>

      </div><!--end card-header class-->

      <div class="card-body">

        <!--input filed for filtering the data in table-->
        <input type="text"  class="form-control pull-right mb-2 filter" placeholder="Filter datas..." id="myInput" >   
       <div class="table-responsive table-min-height">    
          <table class="table table-striped table-bordered" >
            <thead >
          
              <th>Photo</th>
                <th>Spot Name</th>
                <th>Place</th>
                <th>District</th>
                <th>Category</th>
                <th class="text-center">Action</th>
                   
            </thead>
            <tbody id="myTable" >
              <tr v-for="spot in spots">
                <td class="max-spot-photo"><img class="spot-photo" v-bind:src="'<?php echo base_url();?>assets/images/' + spot.photo"></td>
                <td>{{spot.name}}</td>
                <td>{{spot.municipality}}</td>
                <td>{{spot.district}}</td>
                <td>{{spot.category}}</td>
                <td class="min-td">
                        
                  <button class="btn-delete pull-right min-delete"
                    @click="spotInfo.id = spot.id;modalDelete = true;">
                    <span class="fa fa-trash"></span>Delete
                  </button>

                  <button class="btn-edit pull-right" @click="
                    spotInfo.id = spot.id;
                    spotInfo.name = spot.name;
                    spotInfo.municipality = spot.municipality;
                    spotInfo.district = spot.district;
                    spotInfo.category = spot.category;
                    modalEdit = true;">
                    <span class="fa fa-edit"></span> Edit</button>
                    
                </td>
              </tr>
            </tbody>
          </table>
            </div><!--class table-responsive end-->
         </div><!-- class card body end-->      
      </div><!-- class card end-->
  </div><!--class col-lg-10 end-->
</div><!--class row end-->


