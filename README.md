# hadoop utils

## Install

```shell
$ easy_install https://github.com/dgkim84/hutil/archive/master.tar.gz
```

## generating config files

* XML로 설정 파일을 만드는 것은 귀찮으면서 각종 -site.xml 파일을 만들어야 한다.
* 개인적으로 XML은 가독성도 상당히 떨어진다.

발로 짜서 그닥 볼건 없어요. 회사에선 다른걸 쓰고 개인적으로 fabric으로 배포할 때 썼던 라이브러리 중 하나인데 분리했습니다. 에러처리라던지 이런건 없습니다.

```yaml
core:
	fs.default.name: hdfs://localhost:9000
	io.compression.codecs:
		- org.apache.hadoop.io.compress.DefaultCodec
		- org.apache.hadoop.io.compress.GzipCodec
		- org.apache.hadoop.io.compress.BZip2Codec
		- org.apache.hadoop.io.compress.SnappyCodec

hdfs:
	dfs.replication: 3
	dfs.block.size: 268435456
	dfs.name.dir:
		- /data1/dfs/name
		- /data2/dfs/name
```

### Usages

```shell
hutil --help
Usage: hutil [options]

Options:
  -h, --help            show this help message and exit
  -f INFILE, --file=INFILE
                        source configuration file
  -c CHROOT, --chroot=CHROOT
                        change root (only *.yaml)
  -o OUTFILE, --output=OUTFILE
                        output file
  --stdout              stdout
```

```shell
$ hutil -f sites.yaml -c core --stdout
$ hutil -f sites.yaml -c core -o core-site.xml
$ hutil -f sites.yaml -c core -o hdfs-site.xml
$ hutil -f sites.yaml -c mapred -o mapred-site.xml

$ hutil -f sites.yaml -c core -o core-site.xml
$ hutil -f core-site.xml -o core-site.yaml
$ hutil -f core-site.yaml -o core-site.xml
```
input이 yaml이면 xml이 결과로 나오고 xml이면 yaml이 결과로 나옵니다. yaml의 경우는 xml로 만들 때 root로 사용할 키를 지정할 수 있고 하나의 yaml로 여러 xml파일을 뽑아내기 위함입니다. (귀찮아서...)

## Output

```xml
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>

  <property>
    <name>io.compression.codecs</name>
    <value>org.apache.hadoop.io.compress.DefaultCodec,org.apache.hadoop.io.compress.GzipCodec,org.apache.hadoop.io.compress.BZip2Codec,org.apache.hadoop.io.compress.SnappyCodec</value>
  </property>

  <property>
    <name>fs.default.name</name>
    <value>hdfs://localhost:9000</value>
  </property>

</configuration>
```
