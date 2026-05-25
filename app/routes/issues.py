from fastapi import APIRouter,HTTPException,status
import uuid
from app.schemas import IssueCreate,IssueOut, IssueStatus,IssueUpdate
from app.storage import load_data,save_data

router=APIRouter(prefix="/api/issues",tags=["issues"])

@router.get("/",response_model=list[IssueOut])
def get_issues():
    issues=load_data()
    return issues

@router.post("/", response_model=IssueOut,status_code=status.HTTP_201_CREATED)
def create_issues(issue: IssueCreate):
    issues=load_data()
    new_issue={
        "id":str(uuid.uuid4()),
        "title":issue.title,
        "description":issue.description,
        "priority":issue.priority,
        "status":IssueStatus.open
    }
    issues.append(new_issue)
    save_data(issues)
    return new_issue

@router.get("/{issue_id}",response_model=IssueOut)
def get_issue(issue_id:str):
    issues=load_data()
    for issue in issues:
        if issue["id"]==issue_id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")


@router.put("/{issue_id}", response_model=IssueOut)
def update_issue(issue_id:str,issueP:IssueUpdate):
    issues=load_data()
    for index,issue in enumerate(issues):
        if issue["id"]==issue_id:
            updated_issue=issue.copy()
            if issueP.title is not None:
                updated_issue["title"]=issueP.title
            if issueP.description is not None:
                updated_issue["description"]=issueP.description 
            if issueP.priority is not None:
                updated_issue["priority"]=issueP.priority
            if issueP.status is not None:
                updated_issue["status"]=issueP.status
            issues[index]=updated_issue
            save_data(issues)
            return updated_issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.delete("/{issue_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id: str):
    issues=load_data()
    for index,issue in enumerate(issues):
        if issue["id"]==issue_id:
            issues.pop(index)
            save_data(issues)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

    