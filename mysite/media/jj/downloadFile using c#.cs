OpenFileDialog ofd = new OpenFileDialog();
ofd.ShowDialog();

// download file using c#
WebClient wc = new WebClient();

wc.DownlaodFileCompleted += new AsyncCompletedEventHandlder(FileDownloadCompleted);
Uri img = new Uri(txtbox.Text);

wc.DownloadFileAsync(img, "Download.png");
d
//call this function for download status
private void FileDownloaCompleted(){
	// message
}

	//delete file


// save file dialog
SaveFileDialog sfd = new SaveFileDialog();

if(save.ShowDialog() == DialogResult.OK){
	StreamWriter write = new StreamWriter(File.Create(save.Filename));

	write.Write(txtbox);
	write.Dispose();

	File.Delete(path/filename)