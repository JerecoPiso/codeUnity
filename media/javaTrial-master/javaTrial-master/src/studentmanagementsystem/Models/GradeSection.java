/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package studentmanagementsystem.Models;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.ResultSet;
import javax.swing.JOptionPane;
/**
 *
 * @author User
 */
public class GradeSection extends Connection{
    //inialize variable
    public String gradesec;
    public int id;
    
     public GradeSection(){}
    
     public GradeSection(int id, String gradesec){
         this.id =id;
         this.gradesec = gradesec;
     }
     public GradeSection(String gradesec){
       
         this.gradesec = gradesec;
     }
     //setters
     public void setId(int id){
         this.id = id;
     }
     public void setGradesec(String gradesec){
         this.gradesec = gradesec;
     }
     //getters
     public int getId(){
         return this.id;
     }
      public String getGradesec(){
         return this.gradesec;
     }
      
       //adding new grade and section to database
    public int addGradeSec() throws SQLException{
         
        try{
            PreparedStatement stmt = this.conn.prepareStatement("INSERT INTO gradeSection (gradesec) VALUES (?)");
            stmt.setString(1, this.gradesec);
            
            return stmt.executeUpdate();
        }catch(SQLException e){
            
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            
            return 0;
        }
    }
    public int deleteGradeSection(int id){
        try{
            PreparedStatement stmt = this.conn.prepareStatement("DELETE FROM gradeSection WHERE id = ?");
            stmt.setInt(1, id);
            return stmt.executeUpdate();
        }catch(SQLException e){
            
            JOptionPane.showMessageDialog(null,e.getSQLState(), "Error", JOptionPane.ERROR_MESSAGE);
            return 0;
        }
    }
    public int editGradeSection(int id,String gradesec){
        
        try{
            PreparedStatement stmt = this.conn.prepareStatement("UPDATE gradeSection SET gradesec = ? WHERE id = ?");
            stmt.setString(1, gradesec);
            stmt.setInt(2, id);
            return stmt.executeUpdate();
        }catch(SQLException e){
             JOptionPane.showMessageDialog(null,e.getSQLState(),"Error", JOptionPane.ERROR_MESSAGE);
             return 0;
        }
        
    }
     public ResultSet gradesecChecker(){
         
         try{
             PreparedStatement stmt = this.conn.prepareStatement("SELECT * FROM gradeSection WHERE gradesec = ?");
             stmt.setString(1, this.gradesec);
             return stmt.executeQuery();
         }catch(SQLException e){
             
             JOptionPane.showMessageDialog(null,e.getSQLState(),"Error", JOptionPane.ERROR_MESSAGE);
             return null;
         }
         
     }
     //get all the grade and section from the database
     public ResultSet getGradeandSection(){
        try{
            
            PreparedStatement stmt = this.conn.prepareStatement("SELECT * FROM gradeSection");
            return stmt.executeQuery();
            
        }catch(SQLException e){
             JOptionPane.showMessageDialog(null,"Error in getting datas!", "Error", JOptionPane.ERROR_MESSAGE);
             
             return null;
             
        }
        
    }
  
}
