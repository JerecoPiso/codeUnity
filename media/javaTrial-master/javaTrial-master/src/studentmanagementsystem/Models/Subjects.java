/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package studentmanagementsystem.Models;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.swing.JOptionPane;
/**
 *
 * @author User
 */
public class Subjects extends Connection{
    public int id;
    public String subject, subjectgrade;
    
    public Subjects(){}
    
    public Subjects(int id, String subject, String gradesec){
         this.id = id;
         this.subject = subject;
         this.subjectgrade = gradesec;
    }
    public Subjects(String sub){
        this.subject = sub;
    }
    
    public void setId(int id){
        this.id = id;
    }
    public void setSubject(String sub){
        this.subject = sub;
    }
    public void setSubjectgrade(String gradesec){
        this.subjectgrade = gradesec;
       
    }
    
    
    public int getId(){
       return this.id;
    }
    public String getSubject(){
       return this.subject;
    }
    public String getSubjectgrade(){
       return this.subjectgrade;
    }
    public int addSubjects() throws SQLException{
        
       try{
            PreparedStatement stmt = this.conn.prepareStatement("INSERT INTO subjects (subject, gradesec) VALUES(?,?)");
            stmt.setString(1, this.subject);
            stmt.setString(2, this.subjectgrade);
            
            return stmt.executeUpdate();
                    
        }catch(SQLException e){
            
            return 0;
        }
    }
    public int delSubject(int id){
        try{
            PreparedStatement stmt = this.conn.prepareStatement("DELETE FROM subjects WHERE id = ?");
            stmt.setInt(1, id);
         
            
            return stmt.executeUpdate();
        }catch(SQLException e){
            JOptionPane.showMessageDialog(null,e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            
            return 0;
        }
    }
    public int editSubject(int id, String sub, String gradesec){
       try{
           PreparedStatement stmt = this.conn.prepareStatement("UPDATE subjects SET subject = ?, gradesec = ? WHERE id = ?");
           stmt.setString(1, sub);
           stmt.setString(2, gradesec);
           stmt.setInt(3, id);
           return stmt.executeUpdate();
       }catch(SQLException e){
           JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
           
           return 0;
       }
    }
    
    public ResultSet getSubjects(){
        
        try{
            PreparedStatement stmt = this.conn.prepareStatement("SELECT * FROM subjects");
            
            return stmt.executeQuery();
                    
        }catch(SQLException e){
            
            return null;
        }
    }
    public ResultSet getSubjectForGrading(){
         try{
            PreparedStatement stmt = this.conn.prepareStatement("SELECT * FROM subjects WHERE gradesec = ?");
            stmt.setString(1, this.subjectgrade);
            //System.out.print("hahaha" +gradesec+ "hahaha");
            return stmt.executeQuery();
                    
        }catch(SQLException e){
            
            return null;
        }
        
    }
    public ResultSet checkGradeSectionExistInSubjects(String gradesec){
        try{
            
            PreparedStatement stmt = this.conn.prepareStatement("SELECT * FROM subjects WHERE gradesec = ?");
            stmt.setString(1, gradesec);
            
            return stmt.executeQuery();
            
        }catch(SQLException e){
            
            return null;
        }
    }
    public ResultSet subjectChecker(String sub){
        try{
             PreparedStatement stmt = this.conn.prepareStatement("SELECT * FROM subjects WHERE subject = ?");
             stmt.setString(1, sub);
             return stmt.executeQuery();
        }catch(SQLException e){
            
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            return null;
        }
        
    }
}
