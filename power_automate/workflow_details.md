# Prediction Risk Review Workflow Details

Flow name: ISIC Prediction Risk Review

Trigger:
- When a HTTP request is received from the FastAPI app (or scheduled check on database)

Steps:
1. Parse the prediction result (probability, image filename, timestamp)
2. Condition: Is probability between 0.48 and 0.52?
   - Yes → Continue
   - No → End flow
3. Create item in SharePoint list "Prediction Reviews"
   - Columns: ISIC_ID, Probability, Image_Link, Status = "Pending Review"
4. Send Teams message to reviewer channel
   - Include link to the SharePoint item and the uploaded image
5. Wait for reviewer to update the item (Approved / Rejected + comments)
6. Update the original prediction record in the database with reviewer feedback

This workflow demonstrates:
- Microsoft Power Automate integration
- Human-in-the-loop review
- Safe handling of uncertain predictions
