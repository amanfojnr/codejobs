# CodeJobs API
> An open data job listing platform that can be used to build job listing client services for tech related jobs.



CodeJobs offer a shared data interface from job postings by companies all around the world. It does this by providing endpoints, that developers can build client apps on and registered companies can use to create company profiles and post job openings. There are endpoints for listing the data as well. So there are possibilities of a wider reach with several clients displaying common data at different places.

![](https://s8.postimg.org/9arrqheol/codelabs.png)


## Usage example
_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

The service is built with Django and the djangorestframework. Dependencies are available in there requirements.txt file.

OS X & Linux & Windows:

```sh
git clone https://github.com/amanfojnr/codejobs.git
cd codejobs
virtualenv -p python3 myvenv
source myvenv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


## Release History

* 0.0.1
    * Work in progress

## Meta

Kenneth Amanfo Junior – [@amanfojnr_](https://twitter.com/amanfojnr_) – amanfojnr@zoho.com

Distributed under the {{ }} license. See ``LICENSE`` for more information.

[https://github.com/amanfojnr](https://github.com/amanfojnr/)

## Contributing

1. Fork it (<https://github.com/amanfojnr/codejobs/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki