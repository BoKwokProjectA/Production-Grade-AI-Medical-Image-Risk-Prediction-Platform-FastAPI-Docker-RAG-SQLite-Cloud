# Power Automate Flow Diagram (Text version)

User Upload Image
        ↓
FastAPI /predict endpoint
        ↓
Get probability
        ↓
Is probability 0.48 - 0.52 ?
     /         \
   Yes          No
    ↓            ↓
Create SharePoint item    End
    ↓
Send Teams notification
    ↓
Reviewer checks & adds feedback
    ↓
Update database with feedback
