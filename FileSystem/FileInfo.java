/**
 * Created by Administrator on 2015/9/20.
 */

import java.io.File;
import java.io.FileFilter;
import java.io.Serializable;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;


public class FileInfo implements Serializable {

    /**
     *
     */
    private static final long serialVersionUID = 1L;
    String name;
    long size;
    Date lastModified;
    int dir;
    int hid;
    int isread;
    int iswritten;
    int isexcute;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public long getSize() {
        return size;
    }

    public void setSize(long size) {
        this.size = size;
    }

    public Date getLastModified() {
        return lastModified;
    }

    public void setLastModified(Date lastModified) {
        this.lastModified = lastModified;
    }

    public int isDir() {
        return dir;
    }

    public void setDir(boolean dir) {
        if(dir == true){
            this.dir = 1;
        }else{
            this.dir = 0;
        }

    }

    //hidden
    public int isHid() {

        return hid;
    }

    public void setHid(boolean hid) {
        if(hid == true){
            this.hid = 1;
        }else{
            this.hid = 0;
        }

    }
    //readable

    public int isRead() {
        return isread;
    }

    public void setRead(boolean isread) {
        if(isread == true){
            this.isread = 1;
        }else{
            this.isread = 0;
        }

    }
    //iswritten

    public int iswritten() {
        return iswritten;
    }


    //isexcute
    public int isexcute(){
        return isexcute;
    }

    public void setexcute(boolean isexcute){
        if(isexcute == true){
            this.isexcute = 1;
        }else{
            this.isexcute = 0;
        }
    }

    public void setwritten(boolean iswritten) {
        if(iswritten == true){
            this.iswritten = 1;
        }else{
            this.iswritten = 0;
        }

    }

    public String PrintAtt(FileInfo fileInfo) {
        String temps;
      //  temps = fileInfo.getName()  + " " + isDir() + " " + isHid() +" "+ isRead() + " "+ iswritten() + " "+ isexcute()+" " + getSize() + " " + getLastModified();

        temps =  isHid() +" "+ isRead() + " "+ iswritten() + " "+ isexcute();
        return temps;
    }

}