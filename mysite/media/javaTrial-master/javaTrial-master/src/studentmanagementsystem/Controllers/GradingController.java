/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package studentmanagementsystem.Controllers;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.Initializable;
import javafx.fxml.FXML;
import javafx.scene.control.ComboBox;
import javafx.scene.control.TextField;
import java.sql.SQLException;
import java.sql.ResultSet;
import java.text.DecimalFormat;
import javafx.scene.control.Button;
import javax.swing.JOptionPane;
import studentmanagementsystem.Models.Subjects;
import studentmanagementsystem.Models.GradeSection;
import studentmanagementsystem.Models.Student;

/**
 * FXML Controller class
 *
 * @author User
 */
public class GradingController implements Initializable {
    @FXML
    public TextField quiz, recitation, exam, project, totalQuiz, totalExam,totalProject,
            totalRecitation,  projectPercent, examPercent, recitationPercent, quizPercent;
    @FXML
    private ComboBox gradesec, subject, students, quarter;
    @FXML
    private Button setFinalGrade;
    @FXML
    private String quarterGrade = "";
    /**
     * Initializes the controller class.
     */
    
    @FXML
    public void setExamPercent(){
        Boolean examm, totalExamm;
        double examAve;
        
        examm = exam.getText().matches("-?\\d+(\\.\\d+)?");
        totalExamm = totalExam.getText().matches("-?\\d+(\\.\\d+)?");
         if(examm != false && totalExamm != false && !exam.getText().equals("") && !totalExam.getText().equals("") && Double.parseDouble(exam.getText()) <= Double.parseDouble(totalExam.getText())){
            DecimalFormat numberFormat = new DecimalFormat("#.00");
            examAve = (Double.parseDouble(exam.getText()) / Double.parseDouble(totalExam.getText()) * 100.00) * .20;
            examPercent.setText(numberFormat.format(examAve)+" % percent.");
        }
        
    }
    @FXML
    public void setRecitationPercent(){
        Boolean recitationn, totalRecitationn;
        double recitationAverage;
        recitationn = recitation.getText().matches("-?\\d+(\\.\\d+)?");
        totalRecitationn = totalRecitation.getText().matches("-?\\d+(\\.\\d+)?");
        if(recitationn != false && totalRecitationn != false && !recitation.getText().equals("") && !totalRecitation.getText().equals("") && Double.parseDouble(recitation.getText()) <= Double.parseDouble(totalRecitation.getText())){
            DecimalFormat numberFormat = new DecimalFormat("#.00");
            recitationAverage = (Double.parseDouble(recitation.getText()) / Double.parseDouble(totalRecitation.getText()) * 100.00) * .40;
            recitationPercent.setText(numberFormat.format(recitationAverage)+" % percent.");
        }
    }
    @FXML
    public void setProjectPercent(){
        Boolean projectt, totalProjectt;
        double projectAve;
        projectt = project.getText().matches("-?\\d+(\\.\\d+)?");
        totalProjectt = totalProject.getText().matches("-?\\d+(\\.\\d+)?");
        
        if(projectt != false && totalProjectt != false && !project.getText().equals("") && !totalProject.getText().equals("") && Double.parseDouble(project.getText()) <= Double.parseDouble(totalProject.getText())){
            DecimalFormat numberFormat = new DecimalFormat("#.00");
            projectAve = (Double.parseDouble(project.getText()) / Double.parseDouble(totalProject.getText()) * 100.00) * .20;
            projectPercent.setText(numberFormat.format(projectAve)+" % percent.");
        }
        
    }
    @FXML
    public void setQuizPercent(){
        Boolean quizz, totalQuizz;
        double quizAve;
        quizz = quiz.getText().matches("-?\\d+(\\.\\d+)?");
        totalQuizz = totalQuiz.getText().matches("-?\\d+(\\.\\d+)?");
        if(quizz != false && totalQuizz != false && !quiz.getText().equals("") && !totalQuiz.getText().equals("") && Double.parseDouble(quiz.getText()) <= Double.parseDouble(totalQuiz.getText())){
             DecimalFormat numberFormat = new DecimalFormat("#.00");
            quizAve = (Double.parseDouble(quiz.getText()) / Double.parseDouble(totalQuiz.getText()) * 100.00) * .20;
             quizPercent.setText(numberFormat.format(quizAve)+" % percent.");
        }
    }
    @FXML
    public void setGrade(){
        double average, quizAve, examAve, projectAve, recitationAve;
        Boolean quizz, totalQuizz, examm, totalExamm,  projectt, totalProjectt, recitationn, totalRecitationn;
        if(!quarterGrade.equals("")){
                quizz = quiz.getText().matches("-?\\d+(\\.\\d+)?");
                totalQuizz = totalQuiz.getText().matches("-?\\d+(\\.\\d+)?");
                examm = exam.getText().matches("-?\\d+(\\.\\d+)?");
                totalExamm = totalExam.getText().matches("-?\\d+(\\.\\d+)?");
                projectt = project.getText().matches("-?\\d+(\\.\\d+)?");
                totalProjectt = totalProject.getText().matches("-?\\d+(\\.\\d+)?");
                recitationn = recitation.getText().matches("-?\\d+(\\.\\d+)?");
                totalRecitationn = totalRecitation.getText().matches("-?\\d+(\\.\\d+)?");

                if(quizz == false || totalQuizz == false){
                   JOptionPane.showMessageDialog(null, "You should only input numbers in the quiz and total score!","Error",JOptionPane.ERROR_MESSAGE);
                }else if(examm  == false || totalExamm == false){
                   JOptionPane.showMessageDialog(null, "You should only input numbers exam and total score!","Error",JOptionPane.ERROR_MESSAGE);
                }else if(projectt == false || totalProjectt  == false){
                   JOptionPane.showMessageDialog(null, "You should only input numbers project and total score!","Error",JOptionPane.ERROR_MESSAGE);
                }else if(recitationn  == false || totalRecitationn  == false){
                   JOptionPane.showMessageDialog(null, "You should only input numbers recitation and total score!","Error",JOptionPane.ERROR_MESSAGE); 
                }else{


                        if(quiz.getText().equals("") || totalQuiz.getText().equals("")){

                            JOptionPane.showMessageDialog(null, "Quiz score must not be empty!", "Error", JOptionPane.ERROR_MESSAGE);

                        }else if(recitation.getText().equals("") || totalRecitation.getText().equals("")){

                            JOptionPane.showMessageDialog(null, "Recitation score must not be empty!", "Error", JOptionPane.ERROR_MESSAGE);
                        }else if(exam.getText().equals("") || totalExam.getText().equals("")){

                            JOptionPane.showMessageDialog(null, "Exam score must not be empty!", "Error", JOptionPane.ERROR_MESSAGE);
                        }else if(project.getText().equals("") || totalProject.getText().equals("")){
                            JOptionPane.showMessageDialog(null, "Project score must not be empty!", "Error", JOptionPane.ERROR_MESSAGE);

                        }else{
                             if(Double.parseDouble(quiz.getText()) > Double.parseDouble(totalQuiz.getText())){

                                JOptionPane.showMessageDialog(null, "Quiz score must not be greater than total score", "Error" ,JOptionPane.ERROR_MESSAGE);

                            }else if(Double.parseDouble(exam.getText()) > Double.parseDouble(totalExam.getText())){

                                JOptionPane.showMessageDialog(null, "Exam's score must not be greater than total score", "Error" ,JOptionPane.ERROR_MESSAGE);

                            }else if(Double.parseDouble(project.getText()) > Double.parseDouble(totalProject.getText())){

                                JOptionPane.showMessageDialog(null, "Project's score must not be greater than total score", "Error" ,JOptionPane.ERROR_MESSAGE);

                            }else if(Double.parseDouble(recitation.getText()) > Double.parseDouble(totalRecitation.getText())){

                                JOptionPane.showMessageDialog(null, "Recitation's score must not be greater than total score", "Error" ,JOptionPane.ERROR_MESSAGE);

                            }else{
                                DecimalFormat numberFormat = new DecimalFormat("#.00");
                                 quizAve = (Double.parseDouble(quiz.getText()) / Double.parseDouble(totalQuiz.getText()) * 100.00) * .20;
                                 examAve = (Double.parseDouble(exam.getText()) / Double.parseDouble(totalExam.getText()) * 100.00) * .20;
                                 projectAve = (Double.parseDouble(project.getText()) / Double.parseDouble(totalProject.getText()) * 100.00) * .20;
                                 recitationAve = (Double.parseDouble(recitation.getText()) / Double.parseDouble(totalRecitation.getText()) * 100.00) * .40;
                                 average = quizAve + examAve + projectAve + recitationAve;

                                 examPercent.setText(numberFormat.format(examAve)+" % percent.");
                                 projectPercent.setText(numberFormat.format(projectAve)+" % percent.");
                                 recitationPercent.setText(numberFormat.format(recitationAve)+" % percent.");

                                 //limit the decimal places of the average grade

                                JOptionPane.showMessageDialog(null, numberFormat.format(average), "Grade", JOptionPane.INFORMATION_MESSAGE);
                                System.out.print(gradesec.getValue().toString() + " "+ subject.getValue().toString()
                                + " " + students.getValue().toString() + " " + quarter.getValue().toString()
                                );
                            }

                        }

                }
            
            
            
        }else{
              JOptionPane.showMessageDialog(null,"Select Quarter for the Grade to be saved!", "Grade", JOptionPane.ERROR_MESSAGE);
        }
     
    }
    @FXML
    public void getGradesec(){
        
        try{
            GradeSection gradesection = new GradeSection();
            Subjects sub = new Subjects();
            
            ResultSet res = gradesection.getGradeandSection();
            ResultSet ret;
            while(res.next()){
                 ret = sub.checkGradeSectionExistInSubjects(new GradeSection(res.getString("gradesec")).getGradesec());
                   if(ret.next()){
                      gradesec.getItems().addAll(new GradeSection(res.getString("gradesec")).getGradesec());
                   }
                //gradesec.getItems().addAll(new GradeSection(res.getString("gradesec")).getGradesec());
            }
            
        }catch(SQLException e){
            
            JOptionPane.showMessageDialog(null,e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            
        }
    }
    @FXML
    public void setSubject(){ 
       try{
           //CREATE INSTANCE OF SUBJECTS
           Subjects sub = new Subjects();
           sub.subjectgrade = gradesec.getValue().toString();
           ResultSet ret = sub.getSubjectForGrading();
          
           //clear the combobox of the subjects to avoid repetition of datas
           subject.getSelectionModel().clearSelection();
           subject.getItems().clear();
           subject.setDisable(false);
           while(ret.next()){
                  
                   subject.getItems().addAll(new Subjects(ret.getString("subject")).getSubject());
              
           }
            //setStudent();
            students.setDisable(true);
             setFinalGrade.setDisable(true);
       }catch(SQLException e){
           
           
       }
       
    }
    @FXML
    public void setStudent(){
        try{
           //CREATE INSTANCE OF SUBJECTS
           Student stud = new Student();
            
        
                ResultSet ret = stud.getStudentsForGrading(gradesec.getValue().toString());
       
                //clear the combobox of the subjects to avoid repetition of datas
                students.getSelectionModel().clearSelection();
                students.getItems().clear();
                students.setDisable(false);
              System.out.print(subject.getValue().toString());
                 
                while(ret.next()){

                        students.getItems().addAll(new Student(ret.getString("name")).getName());

                }

               
         
       }catch(SQLException e){
           
           
       }
    }
    @FXML
    public void setQuarter(){
        quarterGrade = quarter.getValue().toString();
    }
    @FXML
    public void chooseStudent(){
          setFinalGrade.setDisable(false);
         
    }
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
        getGradesec();
        quarter.getItems().addAll(
           "1st Quarter",
           "2nd Quarter",
           "3rd Quarter",
           "4th Quarter"
                              
        );
        
    }    
    
}
