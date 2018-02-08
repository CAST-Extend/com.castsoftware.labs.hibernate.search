package Package1;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import org.hibernate.search.annotations.Analyze;
import org.hibernate.search.annotations.ContainedIn;
import org.hibernate.search.annotations.Field;
import org.hibernate.search.annotations.Document;
import org.hibernate.search.annotations.Boost;
import org.hibernate.search.annotations.Index;
import org.hibernate.search.annotations.Store;
import org.hibernate.search.annotations.Spatial;
import org.hibernate.search.annotations.FieldBridge;
import org.hibernate.search.annotations.Index;
import org.hibernate.search.annotations.IndexedEmbedded;


@Entity
@Indexed
@Table(name = "EMPLOYEE")
public class Employee {

   @Id
   @GeneratedValue(strategy = GenerationType.IDENTITY)
   @Column(name = "EMP_ID")
   private long id;
   
   	@Column(length = 10000)
	public String getDescription() { return description; }


   @Field(index = Index.YES, analyze = Analyze.NO, store = Store.NO)
   @Column(name = "NAME", nullable = false)
   private String name;

   @Column(name = "DESIGNATION")
   private String designation;
   
   @Document
   private String designationone;
   
   @Field(name="Abstract", index=Index.TOKENIZED, store=Store.YES, boost=@Boost(2f))
   @Boost(1.5f)
   public String getSummary() { return summary; }

   @IndexedEmbedded(depth = 1, prefix = "ownedBy_")
   private Owner ownedBy;
    
   
   @Field(analyze = Analyze.NO)
   @Spatial
   public Coordinates getLocation() {
   	
   	}

   @ContainedIn
   @ManyToOne
   @JoinColumn(name = "DPT_ID")
   private Department department;

   public Employee() {
   }
   
   @FieldBridge
   public long getId() {
      return id;
   }

   public void setId(long id) {
      this.id = id;
   }

   public String getName() {
      return name;
   }

   public void setName(String name) {
      this.name = name;
   }

   public String getDesignation() {
      return designation;
   }

   public void setDesignation(String designation) {
      this.designation = designation;
   }

   public Department getDepartment() {
      return department;
   }

   public void setDepartment(Department department) {
      this.department = department;
   }
}
