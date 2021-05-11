/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package studentmanagementsystem.Controllers;

import java.io.IOException;
import studentmanagementsystem.Models.Student;
import java.net.URL;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ResourceBundle;
import javafx.fxml.Initializable;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.stage.Stage;
import javax.swing.JOptionPane;
import studentmanagementsystem.Models.GradeSection;
import studentmanagementsystem.Models.Subjects;



/**
 * FXML Controller class
 *
 * @author User
 */
public class AdminManageController implements Initializable {
    
    //inialize variables
    @FXML
    private TextField gradSecInput, subject;
    @FXML
    public TableView<Student> studentTable;
    public TableView<GradeSection> gradeSecTable;
    public TableView<Subjects> subjectTable;
    @FXML
    private TableColumn<Integer, Student> colid, idGradeSecTable, idSubjectTable;
    @FXML
    private TableColumn<String, Student> colname, coladdress, colgradesec, colgender, colreligion, colbdate, nameGradeSecTable, nameSubjectTable, gradesecSubjectTable;
    @FXML
    private ComboBox gradeAndSection;
    @FXML
    private Button add, addGradesecBtn, editGradesecBtn, addSubBtn, editSubBtn;
    /**
     * Initializes the controller class.
     */
     @FXML
    public void openAddStudentFrom(){
         
         try{
           
            FXMLLoader fxmlloader = new FXMLLoader(getClass().getResource("FXMLS/AddEditStudent.fxml"));
           
            //Parent root1 = (Parent) fxmlloader.load();
            Stage addStudent = new Stage();
            addStudent.initOwner(add.getScene().getWindow());
            addStudent.setScene(new Scene((Parent) fxmlloader.load()));
            addStudent.setTitle("Student Registrationn");
            addStudent.setResizable(false);
            
            StudentCrudController con = fxmlloader.getController();
            //hide the edit button
            con.edit.setVisible(false);
           
            addStudent.showAndWait();
            
            //call the function load to refresh the table
            load();
           
        } catch(IOException e) {
            
             JOptionPane.showMessageDialog(null,e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            
            
        }
        
    }
    @FXML
    public void openGradingForm(){
        try{
            FXMLLoader loader = new FXMLLoader(getClass().getResource("FXMLS/Grading.fxml"));
            Stage grading = new Stage();
            grading.initOwner(add.getScene().getWindow());
            grading.setScene(new Scene ((Parent) loader.load()));
            grading.setTitle("Grading");
            grading.setResizable(false);
            
            GradingController grade = loader.getController();
          
            grading.showAndWait();
            
        }catch(IOException e){
            JOptionPane.showMessageDialog(null,e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            
        }
    }
    
    
    @FXML
    public void openEditStudentFrom(){
        // int ret;
         Student stud = studentTable.getSelectionModel().getSelectedItem();
         if(stud != null){
             
             try{
           
                FXMLLoader fxmlloader = new FXMLLoader(getClass().getResource("FXMLS/AddEditStudent.fxml"));

                //Parent root1 = (Parent) fxmlloader.load();
                Stage login = new Stage();
                login.initOwner(add.getScene().getWindow());


                login.setScene(new Scene((Parent) fxmlloader.load()));
                login.setTitle("Edit Student");
                login.setResizable(false);
                //create an object of the class studentcruddontroller
                StudentCrudController con = fxmlloader.getController();
                //hide the add button
                con.add.setVisible(false);
                //assign values to the variables of class studentcruddontroller to be sent to the student.java
                con.id = stud.getId();
                con.uname.setText(stud.getName());
                con.address.setText(stud.getAddress());
                con.gradeSec.setValue(stud.getGradesec());
                con.religion.setValue(stud.getReligion());
                con.gender.setValue(stud.getGender());
              
                 
                login.showAndWait();

                //call the function load to refresh the table
                load();
           
            } catch(IOException e) {

                e.printStackTrace();

            }
             
         }else{
             
             JOptionPane.showMessageDialog(null,"Select data to edit!", "Error", JOptionPane.ERROR_MESSAGE);
         }
         
        
    }
    @FXML
    public void addSubject(){
        int ret;
         Subjects subjects = new Subjects();
     
       if(subject.getText().equals("")){
         JOptionPane.showMessageDialog(null,"Subject must not be empty!", "Error", JOptionPane.ERROR_MESSAGE);
       }else if(gradeAndSection.getValue().toString().equals("")){
        JOptionPane.showMessageDialog(null,"Grade and Section must not be empty!", "Error", JOptionPane.ERROR_MESSAGE); 
           
       }else{
            try{
             ResultSet checker = subjects.subjectChecker(subject.getText());
             
              if(checker.next()){
                   JOptionPane.showMessageDialog(null,subject.getText()+ " already exist!", "Error", JOptionPane.ERROR_MESSAGE);
              }else{
                  
                   try{
                       
                       
                        subjects.subject = subject.getText();

                        subjects.subjectgrade = gradeAndSection.getValue().toString();
                        ret =  subjects.addSubjects();
                        if(ret > 0){

                            JOptionPane.showMessageDialog(null,"Added successfully!", "Success", JOptionPane.INFORMATION_MESSAGE);
                            subject.setText("");
                            gradeAndSection.setValue("");
                            loadSubject();
                        }else{
                             JOptionPane.showMessageDialog(null,"Error!", "Error", JOptionPane.ERROR_MESSAGE);

                        }
                   }catch(SQLException e){


                }
        
                  
        }
                
       }catch(SQLException err){
           
           JOptionPane.showMessageDialog(null, err.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
       }
       
           
       }
    
      
    }
     //open the signup form for adding student
    @FXML
    public void addGradeSec(){
        GradeSection gradesec = new GradeSection();
        gradesec.gradesec = gradSecInput.getText();
        
        int ret;
          if(!gradSecInput.getText().equals("")){
                 try{
                    //call the function gradesecChecker to check if the inputted grade & section already exist
                   ResultSet data = gradesec.gradesecChecker();

                   //check if the return data is not null
                   if(data.next()){

                        JOptionPane.showMessageDialog(null, gradSecInput.getText() + " already exist!", "Error", JOptionPane.ERROR_MESSAGE);

                   }else{

                       try{
                           ret = gradesec.addGradeSec();

                           //check if the return data is greater than 0 to check if the query is successful
                           if(ret > 0){
                                JOptionPane.showMessageDialog(null, "Grade & Section is addded successfully", "Error", JOptionPane.ERROR_MESSAGE);
                           }
                            loadGradesecCombobox();

                       }catch(SQLException e){

                           JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
                       }

                   }


                }catch(SQLException err){

                     JOptionPane.showMessageDialog(null, err.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);

                }
                
          }
        
              gradSecInput.setText("");
              //load the table for the grade & section
              loadGradeSec();
        
    }
   
    @FXML
    public void getGradeSec() throws SQLException{
        gradeSecTable.getItems().clear();
        GradeSection gradesection = new GradeSection();
        ResultSet ret = gradesection.getGradeandSection();
      
       
        while(ret.next()){
            gradeSecTable.getItems().add(new GradeSection(ret.getInt("id"), ret.getString("gradesec")
            
            ));
        }
       
    }
    //get all the students
    @FXML
    public void getStudent() throws SQLException{
        studentTable.getItems().clear();
        Student student = new Student();
        ResultSet ret = student.getStudents();
        while(ret.next()){
            studentTable.getItems().add(new Student(ret.getInt("id"), ret.getString("name"), ret.getString("address"), ret.getString("religion"),
                    ret.getString("bdate"), ret.getString("gender"), ret.getString("gradeSec")
            
            ));
        }
        
    }
    //get all the students
    @FXML
    public void getSubjects() throws SQLException{
        subjectTable.getItems().clear();
        Subjects subjects = new Subjects();
        ResultSet ret = subjects.getSubjects();
        while(ret.next()){
            subjectTable.getItems().add(new Subjects(ret.getInt("id"), ret.getString("subject"), ret.getString("gradesec")
            
            ));
        }
    }
    @FXML
    public void deleteSubject(){
        int ret;
        Subjects sub = subjectTable.getSelectionModel().getSelectedItem();
       
        if(sub != null){
            
            Subjects subj = new Subjects();
            ret = subj.delSubject(sub.getId());
            
            if(ret > 0){
                JOptionPane.showMessageDialog(null, "Deleted successfully", "Success", JOptionPane.INFORMATION_MESSAGE);
                loadSubject();
            }else{
                  JOptionPane.showMessageDialog(null, "Error in deleting data!", "Error", JOptionPane.INFORMATION_MESSAGE);
            }
            
            
            
        }else{
            
             JOptionPane.showMessageDialog(null, "Please select data to delete!", "Error", JOptionPane.INFORMATION_MESSAGE);
        }
        
        
    }
    //function for deleting grade & section 
    @FXML
    public void deleteGradeSec(){
        int ret;
        
        GradeSection gradesec = gradeSecTable.getSelectionModel().getSelectedItem();
        
        if(gradesec != null){
            
            GradeSection gradeSection = new GradeSection();
            ret = gradeSection.deleteGradeSection(gradesec.getId());
            
            if(ret > 0){
                
                JOptionPane.showMessageDialog(null, "Deleted successfully", "Error", JOptionPane.INFORMATION_MESSAGE);
                loadGradeSec();
                loadGradesecCombobox();
            }else{
                
                 JOptionPane.showMessageDialog(null, "An error has occurred!", "Error", JOptionPane.ERROR_MESSAGE);
            }
            
        }else{
            
             JOptionPane.showMessageDialog(null, "Please select data to delete!", "Error", JOptionPane.INFORMATION_MESSAGE);
        }
        
    }
    //function for deleting students record
    @FXML
    public void delete(){
       int ret;
       Student stud = studentTable.getSelectionModel().getSelectedItem();
       
       //check if the user selection of data is not equal to null
       if(stud != null){
           Student student = new Student();
           ret = student.deleteStudent(stud.getId());
           
           if(ret > 0){
              
                JOptionPane.showMessageDialog(null,"Deleted successfully!", "Success", JOptionPane.INFORMATION_MESSAGE);
                //call the function load to refresh the table
                load();
                
           }else{
               
                JOptionPane.showMessageDialog(null,"An error has occured!", "Error", JOptionPane.ERROR_MESSAGE);
           }
           
       }else{
           
           JOptionPane.showMessageDialog(null,"Please select data to delete!", "Error", JOptionPane.ERROR_MESSAGE);
       }
        
    }
    @FXML
    public void setDataToEdit(){
        
        GradeSection gradesec = gradeSecTable.getSelectionModel().getSelectedItem();
        
            if(gradesec != null){
              addGradesecBtn.setVisible(false);
              editGradesecBtn.setVisible(true);
           
              
              gradSecInput.setText(gradesec.getGradesec());
            
            }else{

                JOptionPane.showMessageDialog(null,"Please select data to edit!", "Error", JOptionPane.ERROR_MESSAGE);

            }
    }
    @FXML
    public void setSubjectEdit(){
        Subjects sub = subjectTable.getSelectionModel().getSelectedItem();
        if(sub != null){
            subject.setText(sub.getSubject());
            gradeAndSection.setValue(sub.getSubjectgrade());
            addSubBtn.setVisible(false);
            editSubBtn.setVisible(true);            
            
        }else{

                JOptionPane.showMessageDialog(null,"Please select data to edit!", "Error", JOptionPane.ERROR_MESSAGE);

            }
        
    }
    @FXML
    public void editSubject(){
        int ret;
        Subjects subjects = new Subjects();
        Subjects sub = subjectTable.getSelectionModel().getSelectedItem();
          try{
             if(subject.getText().equals(sub.getSubject())){
                 
                 JOptionPane.showMessageDialog(null,"Nothing has changed!", "Error", JOptionPane.ERROR_MESSAGE);
             }else{
                 
              ResultSet checker = subjects.subjectChecker(subject.getText());
             
              if(checker.next()){
                   JOptionPane.showMessageDialog(null,subject.getText()+ " already exist!", "Error", JOptionPane.ERROR_MESSAGE);
              }else{
                  
                  
                    ret = sub.editSubject(sub.getId(), subject.getText(), gradeAndSection.getValue().toString());
                    if(ret > 0){
                        JOptionPane.showMessageDialog(null, "Updated successfully", "Success", JOptionPane.INFORMATION_MESSAGE);
                         addSubBtn.setVisible(true);
                         editSubBtn.setVisible(false);
                         subject.setText("");
                         gradeAndSection.setValue("");

                        loadSubject();
                    }else{
                         JOptionPane.showMessageDialog(null,"An error has occured!", "Error", JOptionPane.ERROR_MESSAGE);
                    }
                  
              }
                 
             }
             
          }catch(SQLException err){
              
                JOptionPane.showMessageDialog(null,err.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
          }
       
    }
    @FXML
    public void editGradeSec(){
        int ret;
      GradeSection gradesec = gradeSecTable.getSelectionModel().getSelectedItem();
       try{ 
           if(gradesec.getGradesec().equals(gradSecInput.getText())){
                  JOptionPane.showMessageDialog(null, "Nothing has chnaged!", "Error", JOptionPane.ERROR_MESSAGE);
           }else{
               
                //call the function gradesecChecker to check if the inputted grade & section already exist
                GradeSection gradesection = new GradeSection();
                gradesection.gradesec = gradSecInput.getText();
             ResultSet data = gradesection.gradesecChecker();

            //check if the return data is not null
             if(data.next()){

                 JOptionPane.showMessageDialog(null, gradSecInput.getText() + " already exist!", "Error", JOptionPane.ERROR_MESSAGE);

             }else{
                 ret = gradesec.editGradeSection(gradesec.getId(),gradSecInput.getText());
               
                if(ret > 0){

                 JOptionPane.showMessageDialog(null, "Updated successfully", "Error", JOptionPane.INFORMATION_MESSAGE);
                 addGradesecBtn.setVisible(true);
                 editGradesecBtn.setVisible(false);


                 gradSecInput.setText("");
                 loadGradeSec();
                 loadGradesecCombobox();
                }else{
                      JOptionPane.showMessageDialog(null,"An error has occured!", "Error", JOptionPane.ERROR_MESSAGE);
                }
           
                     
             }
               
           }
           
       }catch(SQLException err){
           
           
       }
        
        
    }
    //load table and put values in to each columns
    @FXML
    public void loadStudentTable(){
        colid.setCellValueFactory(new PropertyValueFactory("id"));
        colname.setCellValueFactory(new PropertyValueFactory("name"));
        colgradesec.setCellValueFactory(new PropertyValueFactory("gradesec"));
        colbdate.setCellValueFactory(new PropertyValueFactory("bdate"));
        coladdress.setCellValueFactory(new PropertyValueFactory("address"));
        colreligion.setCellValueFactory(new PropertyValueFactory("religion"));
        colgender.setCellValueFactory(new PropertyValueFactory("gender"));    
    }
    //for the table of grade & section
    @FXML
    public void loadGradeSecTable(){
        idGradeSecTable.setCellValueFactory(new PropertyValueFactory("id"));
        nameGradeSecTable.setCellValueFactory(new PropertyValueFactory("gradesec"));
      
    }
    //for the table of grade & section
    @FXML
    public void loadSubjectTable(){
        idSubjectTable.setCellValueFactory(new PropertyValueFactory("id"));
        nameSubjectTable.setCellValueFactory(new PropertyValueFactory("subject"));
        gradesecSubjectTable.setCellValueFactory(new PropertyValueFactory("subjectgrade"));
    }
    @FXML
    public void load(){
        
        try{
            
            getStudent();
                    
        }catch(SQLException e){
            
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            
        }
            loadStudentTable();     
    }
     @FXML
    public void loadGradeSec(){
          
        try{
        
          getGradeSec();
                    
        }catch(SQLException e){
            
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            
        }
            loadGradeSecTable();     
       
    }
    @FXML
    public void loadSubject(){
        
        try{
            
          getSubjects();
                    
        }catch(SQLException e){
            
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            
        }
            loadSubjectTable();     
    }
    @FXML
    public void loadGradesecCombobox(){
        try{
           gradeAndSection.getSelectionModel().clearSelection();
           gradeAndSection.getItems().clear();
        GradeSection gradesection = new GradeSection();
        ResultSet ret = gradesection.getGradeandSection();
        ResultSet res = gradesection.getGradeandSection();
      
         while(ret.next()){
            gradeAndSection.getItems().addAll(new GradeSection(ret.getString("gradesec")).getGradesec());
           
         }
        
       }catch(SQLException e){
           JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
           
       }
        
    }
     @FXML
   
    @Override
    public void initialize(URL url, ResourceBundle rb) {
//       /loadGradesecforGrading();
       loadGradesecCombobox();
       loadGradeSec();
       loadSubject();
       load();
      
    }    
    
}
