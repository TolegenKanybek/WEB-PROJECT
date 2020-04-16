import {Company} from './app/company'

export interface Vacancy{
    id:number,
    name:string,
    description:Text,
    salary:number,
    company:Company
    /* name=models.CharField(max_length=300)
    description=models.TextField()
    salary=models.FloatField()
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
     */
}