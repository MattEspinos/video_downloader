import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;

public class VideoDownloader extends JFrame implements ActionListener {
    private JLabel urlLabel;
    private JTextField urlField;
    private JLabel sourceLabel;
    private JComboBox<String> sourceBox;
    private JLabel saveLabel;
    private JTextField saveField;
    private JButton downloadButton;

    public VideoDownloader() {
        // Set up the GUI components
        setTitle("Video Downloader");
        setLayout(new GridBagLayout());
        GridBagConstraints c = new GridBagConstraints();

        urlLabel = new JLabel("URL:");
        c.gridx = 0;
        c.gridy = 0;
        add(urlLabel, c);

        urlField = new JTextField(20);
        c.gridx = 1;
        c.gridy = 0;
        add(urlField, c);

        sourceLabel = new JLabel("Source:");
        c.gridx = 0;
        c.gridy = 1;
        add(sourceLabel, c);

        String[] sources = {"YouTube", "Instagram"};
        sourceBox = new JComboBox<String>(sources);
        c.gridx = 1;
        c.gridy = 1;
        add(sourceBox, c);

        saveLabel = new JLabel("Save location:");
        c.gridx = 0;
        c.gridy = 2;
        add(saveLabel, c);

        saveField = new JTextField(20);
        c.gridx = 1;
        c.gridy = 2;
        add(saveField, c);

        downloadButton = new JButton("Download");
        c.gridx = 0;
        c.gridy = 3;
        c.gridwidth = 2;
        add(downloadButton, c);
        downloadButton.addActionListener(this);

        pack();
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        // Handle the download button click event
        String url = urlField.getText();
        String source = (String) sourceBox.getSelectedItem();
        String saveLocation = saveField.getText();

        try {
            URL videoUrl = new URL(url);
            InputStream in = videoUrl.openStream();

            // Create a file output stream for the video file
            File videoFile;
            if (!saveLocation.equals("")) {
                videoFile = new File(saveLocation);
            } else {
                videoFile = new File("video.mp4");
            }
            OutputStream out = new FileOutputStream(videoFile);

            // Copy the video stream to the file output stream
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = in.read(buffer)) != -1) {
                out.write(buffer, 0, bytesRead);
            }

            in.close();
            out.close();
        } catch (MalformedURLException ex) {
            JOptionPane.showMessageDialog(this, "Invalid URL", "Error", JOptionPane.ERROR_MESSAGE);
        } catch (IOException ex) {
            JOptionPane.showMessageDialog(this, "Error downloading video", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        VideoDownloader downloader = new VideoDownloader();
    }
}
