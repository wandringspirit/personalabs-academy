Add-Type -AssemblyName System.Windows.Forms

$msg = @"
PERSONALABS ACADEMY - 24-HOUR LEAD FOLLOW-UP REMINDER

1. For Raghav Singh (@raghavsingh7189):
"Hey Raghav! Just checking in—did you manage to open the kit? Let me know if you had any quick questions about how the dancing video workflow works on your phone 🙌"

2. For Siddhesh Jadhav (@siddhesh_786):
"Hey Siddhesh! Did the link work smoothly for you? Let me know which niche you're thinking of building your first AI persona in 🚀"

3. For Prajwal Chengti (@prajwal_chengti):
"Hey Prajwal! Just following up to see if you were able to check out the 5-Day Launch Kit? Let me know if you have any questions on how the Character DNA seed locking works!"
"@

[System.Windows.Forms.MessageBox]::Show($msg, "PersonaLabs Instagram Follow-up", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)
