/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package studentmanagementsystem.Models;

import java.sql.PreparedStatement;
import java.sql.SQLException;
import javax.swing.JOptionPane;
import java.sql.ResultSet;


/**
 *
 * @author User
 */
public class Student extends Connection{
    
    public String name, address, gradesec,religion, gender, bdate;
    public int id;
  
    
    public Student(){}
    
    //constructor for getting the student for grading
    public Student(String student){
        this.name = student;
    }
    //constructor for getting the student for displaying in tableView
    public Student(int id, String name, String address, String religion, String bdate, String gender, String gradeSec){
        this.id = id;
        this.name = name;
        this.address = address;
        this.religion = religion;
        this.bdate = bdate;
        this.gender = gender;
        this.gradesec = gradeSec;
       
 
   }
    public Student(String name, String address, String religion, String bdate, String gender, String gradeSec, int id){
      
        this.name = name;
        this.address = address;
        this.religion = religion;
        this.bdate = bdate;
        this.gender = gender;
        this.gradesec = gradeSec;
        this.id = id;
       
 
   }
   
   //setters
   public void setId(int id){
       this.id = id;
   }
   public void setName(String name){
       this.name = name;
   }
   public void setGradesec(String gradesec){
       this.gradesec = gradesec;
   }
   
   public void setBdate(String bdate){
       this.bdate = bdate;
   }
   
   public void setAddress(String address){
       this.address = address;
   }
   
   public void setReligion(String religion){
       this.religion = religion;
   }
   public void setGender(String gender){
       this.gender = gender;
   }
   
   //getters
   public int getId(){
       return this.id;
   }
   
   public String getName(){
       return this.name;
   }
   
   public String getGradesec(){
       return this.gradesec;
   }
   public String getBdate(){
       
       return this.bdate;
   }
   public String getAddress(){
       return this.address;
   }
   
   public String getReligion(){
       return this.religion;
   }
   
   public String getGender(){
       return this.gender;
   }
   //function for adding students
    public int addStudent(){
        int ret = 0;
        try{
            PreparedStatement stmt = this.conn.prepareStatement("insert into student (name, address, gradeSec,religion, gender, bdate) values (?,?,?,?,?,?)");
            stmt.setString(1, this.name);
            stmt.setString(2, this.address);
            stmt.setString(3, this.gradesec);
            stmt.setString(4, this.religion);
            stmt.setString(5, this.gender);
            stmt.setString(6, this.bdate);
            
            ret = stmt.executeUpdate();
            
            
            
        }catch(SQLException e){
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }
        
        return ret;
    }
    //function for editing the data of a student
    public int studentEdit(){
        int ret = 0;
        try{
            PreparedStatement stmt = this.conn.prepareStatement("UPDATE student SET name = ?, address= ?, gradeSec = ?, religion = ?, gender = ?, bdate = ?  WHERE id = ?");
            stmt.setString(1, this.name);
            stmt.setString(2, this.address);
            stmt.setString(3, this.gradesec);
            stmt.setString(4, this.religion);
            stmt.setString(5, this.gender);
            stmt.setString(6, this.bdate);
            stmt.setInt(7, this.id);
            
            ret = stmt.executeUpdate();
            
            
            
        }catch(SQLException e){
            
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }
        
      
        return ret;
    }
    //function for getting the student to be displayed to tableView
    public ResultSet getStudents(){
        try{
            
            PreparedStatement stmt = this.conn.prepareStatement("SELECT * FROM student");
            return stmt.executeQuery();
            
        }catch(SQLException e){
             JOptionPane.showMessageDialog(null,"Error in getting datas!", "Error", JOptionPane.ERROR_MESSAGE);
             
             return null;
             
        }
        
    }
    //function for deleting students
    public int deleteStudent(int id){
        int ret = 0;
        try{
            PreparedStatement stmt = this.conn.prepareStatement("DELETE FROM student WHERE id= ? ");
            stmt.setInt(1, id);
            
            ret = stmt.executeUpdate();
            
        }catch(SQLException e){
            
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
           
        }
        
        return ret;
    }
    //function for getting students to be put in the combobox for grading
    public ResultSet getStudentsForGrading(String gradesec){
        try{
            
            PreparedStatement stmt = this.conn.prepareStatement("SELECT * FROM student WHERE gradeSec = ?");
            stmt.setString(1, gradesec);
            return stmt.executeQuery();
            
        }catch(SQLException e){
            JOptionPane.showMessageDialog(null,e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            
            return null;
        }
    }
} 
